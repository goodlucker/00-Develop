from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLabel, QAbstractItemView, QMenu
from PyQt5.QtCore import Qt

def create_script_panel(category, script_type, script_groups, show_context_menu, edit_priority, add_scripts, run_selected, delete_selected, view_log):
    panel = QWidget()
    layout = QVBoxLayout(panel)

    list_widget = QListWidget()
    list_widget.setSelectionMode(QAbstractItemView.ExtendedSelection)
    list_widget.setDragDropMode(QListWidget.DropOnly)
    list_widget.setContextMenuPolicy(Qt.CustomContextMenu)
    list_widget.customContextMenuRequested.connect(
        lambda pos: show_context_menu(pos, category, script_type))
    list_widget.itemDoubleClicked.connect(edit_priority)
    script_groups[category][f"{script_type}_widget"] = list_widget

    btn_layout = QHBoxLayout()
    buttons = [
        ("添加脚本", lambda: add_scripts(category, script_type)),
        ("运行选中", lambda: run_selected(category, script_type)),
        ("删除选中", lambda: delete_selected(category, script_type)),
        ("查看日志", lambda: view_log(category, script_type))
    ]

    for text, handler in buttons:
        btn = QPushButton(text)
        btn.clicked.connect(handler)
        btn_layout.addWidget(btn)

    layout.addWidget(QLabel(f"{script_type.upper()} 脚本"))
    layout.addWidget(list_widget)
    layout.addLayout(btn_layout)
    return panel