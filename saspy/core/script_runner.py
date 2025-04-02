import os
import subprocess as sp
import platform as pf
from concurrent.futures import ThreadPoolExecutor, as_completed
from PyQt5.QtCore import QThread, pyqtSignal, QObject
from PyQt5.QtWidgets import QMessageBox


class ScriptRunner(QObject):
    finished = pyqtSignal()

    def __init__(
        self, sas_executable, sas_config, project_path, script_groups, comm, max_workers
    ):
        super().__init__()
        self.sas_executable = sas_executable
        self.sas_config = sas_config
        self.project_path = project_path
        self.script_groups = script_groups
        self.comm = comm
        self.max_workers = max_workers
        self.executor = None
        self.running = False
        self.thread = None  # 添加线程属性

    def run_scripts(self, scripts):
        if self.running:
            QMessageBox.warning(None, "正在运行", "当前有任务正在执行中")
            return

        self.running = True
        self.thread = QThread()
        self.moveToThread(self.thread)
        self.thread.started.connect(lambda: self._execute_scripts(scripts))
        self.thread.finished.connect(self.thread.quit)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()

    def _execute_scripts(self, scripts):
        try:
            self.executor = ThreadPoolExecutor(max_workers=self.max_workers)
            futures = {
                self.executor.submit(self.run_sas_script, script): script
                for script in scripts
            }

            for i, future in enumerate(as_completed(futures)):
                if not self.running:
                    break
                script = futures[future]
                success = future.result()
                if self.comm:
                    self.comm.complete_signal.emit(
                        f"{script['path']}: {status}", success
                    )
                    self.comm.progress_signal.emit(i + 1)
                self.comm.progress_signal.emit(i + 1)
        finally:
            self.running = False
            if self.executor:
                self.executor.shutdown(wait=False)
            self.finished.emit()  # 任务完成后发出信号

    def stop_execution(self):
        if self.running:
            self.running = False
            if self.executor:
                self.executor.shutdown(wait=False)
            QMessageBox.information(None, "已停止", "执行已中止")

    def run_sas_script(self, script):
        script_path = os.path.join(self.project_path, script["path"])
        if not os.path.exists(script_path):
            return False

        try:
            sp.run(
                [
                    self.sas_executable,
                    script_path,
                    "-rsasuser",
                    "-config",
                    self.sas_config,
                    "-log",
                    os.path.splitext(script_path)[0] + ".log",
                    "-print",
                    os.path.splitext(script_path)[0] + ".lst",
                ],
                check=True,
                stdout=sp.DEVNULL,
                stderr=sp.DEVNULL,
            )
            return True
        except sp.CalledProcessError:
            return False
