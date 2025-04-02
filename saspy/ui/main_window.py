from PyQt5.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QGridLayout,
    QTabWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QProgressBar,
    QStatusBar,
    QSpinBox,
    QMessageBox,
    QListWidgetItem,
    QInputDialog,
    QFileDialog,
    QMenu,
    QListWidget,
)
import sys
import os

# 动态添加项目根目录到 sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QColor
import platform as pf
import subprocess as sp
from core.communicate import Communicate
from core.script_runner import ScriptRunner
from core.utils import (
    select_project_path,
    select_sas_executable,
    select_sas_config,
    save_configuration,
    load_configuration,
)
from ui.styles import get_stylesheet
from ui.script_panel import create_script_panel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sas_executable = ""
        self.sas_config = ""
        self.project_path = ""
        self.script_groups = {
            "Metadata": {"dev": [], "qc": [], "dev_widget": None, "qc_widget": None},
            "SDTM": {"dev": [], "qc": [], "dev_widget": None, "qc_widget": None},
            "ADaM": {"dev": [], "qc": [], "dev_widget": None, "qc_widget": None},
            "TLFs": {"dev": [], "qc": [], "dev_widget": None, "qc_widget": None},
            "Other": {"dev": [], "qc": [], "dev_widget": None, "qc_widget": None},
        }
        self.comm = Communicate()
        self.script_runner = ScriptRunner(
            self.sas_executable,
            self.sas_config,
            self.project_path,
            self.script_groups,
            self.comm,
            4,
        )
        self.init_ui()
        self.setup_signals()

    def init_ui(self):
        self.setWindowTitle("SAS Batch Runner - Pro")
        self.setGeometry(100, 100, 1280, 800)
        self.setStatusBar(QStatusBar())
        self.setStyleSheet(get_stylesheet())

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        path_layout = QGridLayout()
        self.create_path_controls(path_layout)

        self.tabs = QTabWidget()
        self.tabs.setStyleSheet("QTabBar::tab { height: 30px; }")
        self.init_tabs()

        control_layout = QHBoxLayout()
        self.create_control_buttons(control_layout)

        self.progress = QProgressBar()
        self.progress.setVisible(False)

        main_layout.addLayout(path_layout)
        main_layout.addWidget(self.tabs)
        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.progress)

        self.setAcceptDrops(True)

    def setup_signals(self):
        self.comm.update_signal.connect(self.update_all_lists)
        self.comm.progress_signal.connect(self.update_progress)
        self.comm.complete_signal.connect(self.show_status)

    def create_path_controls(self, layout):
        self.project_entry = QLineEdit()
        browse_project = QPushButton("浏览...", clicked=self.select_project_path)

        self.sas_exe_entry = QLineEdit()
        browse_sas_exe = QPushButton("浏览...", clicked=self.select_sas_executable)

        self.sas_config_entry = QLineEdit()
        browse_sas_config = QPushButton("浏览...", clicked=self.select_sas_config)

        layout.addWidget(QLabel("项目路径:"), 0, 0)
        layout.addWidget(self.project_entry, 0, 1)
        layout.addWidget(browse_project, 0, 2)
        layout.addWidget(QLabel("SAS可执行文件:"), 1, 0)
        layout.addWidget(self.sas_exe_entry, 1, 1)
        layout.addWidget(browse_sas_exe, 1, 2)
        layout.addWidget(QLabel("SAS配置文件:"), 2, 0)
        layout.addWidget(self.sas_config_entry, 2, 1)
        layout.addWidget(browse_sas_config, 2, 2)

    def init_tabs(self):
        for category in self.script_groups:
            tab = QWidget()
            layout = QHBoxLayout(tab)

            dev_panel = create_script_panel(
                category,
                "dev",
                self.script_groups,
                self.show_context_menu,
                self.edit_priority,
                self.add_scripts,
                self.run_selected,
                self.delete_selected,
                self.view_log,
            )
            qc_panel = create_script_panel(
                category,
                "qc",
                self.script_groups,
                self.show_context_menu,
                self.edit_priority,
                self.add_scripts,
                self.run_selected,
                self.delete_selected,
                self.view_log,
            )

            layout.addWidget(dev_panel)
            layout.addWidget(qc_panel)
            self.tabs.addTab(tab, category)

            # 设置 dev_widget 和 qc_widget
            self.script_groups[category]["dev_widget"] = dev_panel.findChild(
                QListWidget
            )
            self.script_groups[category]["qc_widget"] = qc_panel.findChild(QListWidget)

    def create_control_buttons(self, layout):
        self.max_workers = QSpinBox()
        self.max_workers.setRange(1, 16)
        self.max_workers.setValue(4)

        buttons = [
            ("保存配置", self.save_configuration),
            ("加载配置", self.load_configuration),
            ("开始执行", self.start_execution),
            ("停止执行", self.stop_execution),
        ]

        layout.addWidget(QLabel("最大线程数:"))
        layout.addWidget(self.max_workers)
        layout.addStretch()

        for text, handler in buttons:
            btn = QPushButton(text)
            btn.clicked.connect(handler)
            layout.addWidget(btn)

    def update_all_lists(self):
        for category in self.script_groups:
            for stype in ["dev", "qc"]:
                self.update_list(category, stype)

    def update_list(self, category, script_type):
        list_widget = self.script_groups[category][f"{script_type}_widget"]
        list_widget.clear()
        for script in sorted(
            self.script_groups[category][script_type], key=lambda x: x["priority"]
        ):
            item = QListWidgetItem(f"{script['path']} (优先级: {script['priority']})")
            list_widget.addItem(item)

    def edit_priority(self, item):
        current_text = item.text()
        path_part, _, priority_part = current_text.rpartition("(优先级: ")
        try:
            old_priority = int(priority_part.rstrip(")"))
        except ValueError:
            old_priority = 0

        new_priority, ok = QInputDialog.getInt(
            self, "修改优先级", "输入新的优先级值:", old_priority, 0, 100, 1
        )

        if ok:
            # 获取当前选中的标签页名称
            category = self.tabs.tabText(self.tabs.currentIndex())
            # 判断是 "dev" 还是 "qc"
            list_widget = item.listWidget()
            if list_widget is None:
                QMessageBox.warning(self, "错误", "无法获取关联的列表小部件")
                return
            script_type = "dev" if "DEV" in list_widget.objectName() else "qc"
            # 获取对应的 QListWidget
            list_widget = self.script_groups[category][f"{script_type}_widget"]
            # print(list_widget.objectName())
            # 获取 item 的索引
            index = list_widget.row(item)
            # print(index)

            # 确保索引在有效范围内
            if index == -1 or index >= len(self.script_groups[category][script_type]):
                QMessageBox.warning(self, "索引错误", "选中的脚本索引超出范围")
                return

            # 更新优先级
            self.script_groups[category][script_type][index]["priority"] = new_priority
            # 更新列表显示
            self.update_list(category, script_type)

    def adjust_priority(self, category, script_type, delta):
        selected = self.get_selected_indices(category, script_type)
        scripts = self.script_groups[category][script_type]

        for index in selected:
            new_prio = scripts[index]["priority"] + delta
            scripts[index]["priority"] = max(0, min(100, new_prio))

        self.update_list(category, script_type)

    def set_priority(self, category, script_type, priority):
        selected = self.get_selected_indices(category, script_type)
        for index in selected:
            self.script_groups[category][script_type][index]["priority"] = priority
        self.update_list(category, script_type)

    def handle_dropped_files(self, category, script_type, files):
        valid_files = []
        for file in files:
            if not file.lower().endswith(".sas"):
                continue
            try:
                rel_path = os.path.relpath(file, self.project_path)
                if rel_path.startswith(".."):
                    QMessageBox.warning(self, "路径错误", "文件必须在项目目录内")
                    continue
                valid_files.append({"path": rel_path, "priority": 0})
            except ValueError:
                QMessageBox.warning(self, "路径错误", "无效的文件路径")

        if valid_files:
            self.script_groups[category][script_type].extend(valid_files)
            self.comm.update_signal.emit()

    def view_log(self, category, script_type):
        if selected := self.get_selected_script(category, script_type):
            base_path = os.path.join(self.project_path, selected["path"])
            log_path = os.path.splitext(base_path)[0] + ".log"

            if os.path.exists(log_path):
                if pf.system() == "Darwin":
                    sp.call(("open", log_path))
                elif pf.system() == "Windows":
                    os.startfile(log_path)
                else:
                    sp.call(("xdg-open", log_path))
            else:
                QMessageBox.warning(self, "日志不存在", f"找不到日志文件: {log_path}")

    def update_progress(self, value):
        self.progress.setValue(value)

    def show_status(self, message, success):
        color = QColor(0, 128, 0) if success else QColor(255, 0, 0)
        self.statusBar().showMessage(message)
        self.statusBar().setStyleSheet(f"color: {color.name()};")

    def select_project_path(self):
        path = select_project_path()
        if path:
            self.project_path = path
            self.project_entry.setText(path)

    def select_sas_executable(self):
        path = select_sas_executable()
        if path:
            self.sas_executable = path
            self.sas_exe_entry.setText(path)

    def select_sas_config(self):
        path = select_sas_config()
        if path:
            self.sas_config = path
            self.sas_config_entry.setText(path)

    def save_configuration(self):
        config = {
            "project_path": self.project_path,
            "sas_executable": self.sas_executable,
            "sas_config": self.sas_config,
            "scripts": self.script_groups,
        }
        save_configuration(config)

    def load_configuration(self):
        config = load_configuration(self.script_groups)
        if config:
            self.project_path = config["project_path"]
            self.sas_executable = config["sas_executable"]
            self.sas_config = config["sas_config"]
            self.script_groups = config["scripts"]

            self.project_entry.setText(self.project_path)
            self.sas_exe_entry.setText(self.sas_executable)
            self.sas_config_entry.setText(self.sas_config)
            self.comm.update_signal.emit()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        files = [u.toLocalFile() for u in event.mimeData().urls()]
        current_tab = self.tabs.tabText(self.tabs.currentIndex())
        script_type = "dev" if "DEV" in self.sender().objectName() else "qc"
        self.handle_dropped_files(current_tab, script_type, files)

    def add_scripts(self, category, script_type):
        files, _ = QFileDialog.getOpenFileNames(
            self, "Select SAS Scripts", self.project_path, "SAS Files (*.sas)"
        )
        if files:
            self.handle_dropped_files(category, script_type, files)

    def delete_selected(self, category, script_type):
        list_widget = self.script_groups[category][f"{script_type}_widget"]
        for item in reversed(list_widget.selectedItems()):
            index = list_widget.row(item)
            del self.script_groups[category][script_type][index]
        self.comm.update_signal.emit()

    def run_selected(self, category, script_type):
        selected = [
            self.script_groups[category][script_type][i]
            for i in self.get_selected_indices(category, script_type)
        ]
        self.script_runner.run_scripts(selected)

    def show_context_menu(self, pos, category, script_type):
        menu = QMenu()
        menu.addAction("删除选中", lambda: self.delete_selected(category, script_type))
        menu.addAction("查看日志", lambda: self.view_log(category, script_type))
        menu.exec_(self.sender().mapToGlobal(pos))

    def start_execution(self):
        # 启动脚本执行逻辑
        pass

    def stop_execution(self):
        self.script_runner.stop_execution()

    def get_selected_indices(self, category, script_type):
        list_widget = self.script_groups[category][f"{script_type}_widget"]
        return [list_widget.row(item) for item in list_widget.selectedItems()]

    def get_selected_script(self, category, script_type):
        list_widget = self.script_groups[category][f"{script_type}_widget"]
        selected_items = list_widget.selectedItems()
        if selected_items:
            index = list_widget.row(selected_items[0])
            return self.script_groups[category][script_type][index]
        return None
