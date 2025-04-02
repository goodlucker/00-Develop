import unittest
from unittest.mock import patch, MagicMock
from PyQt5.QtCore import QThread
from saspy.core.script_runner import ScriptRunner


class TestScriptRunner(unittest.TestCase):
    def setUp(self):
        self.sas_executable = "sas"
        self.sas_config = "sas_config.cfg"
        self.project_path = "/path/to/project"
        self.script_groups = []
        self.comm = MagicMock()
        self.max_workers = 2
        self.runner = ScriptRunner(
            self.sas_executable,
            self.sas_config,
            self.project_path,
            self.script_groups,
            self.comm,
            self.max_workers,
        )

    @patch("saspy.core.script_runner.QMessageBox.warning")
    def test_run_scripts_already_running(self, mock_warning):
        self.runner.running = True
        self.runner.run_scripts([])
        mock_warning.assert_called_once_with(None, "正在运行", "当前有任务正在执行中")

    @patch.object(QThread, "start")
    def test_run_scripts_starts_thread(self, mock_start):
        self.runner.running = False
        self.runner.run_scripts([])
        self.assertTrue(self.runner.running)
        mock_start.assert_called_once()

    @patch("saspy.core.script_runner.ThreadPoolExecutor")
    @patch("saspy.core.script_runner.as_completed")
    def test_execute_scripts(self, mock_as_completed, mock_executor):
        mock_future = MagicMock()
        mock_future.result.return_value = True
        mock_as_completed.return_value = [mock_future]
        mock_executor.return_value.__enter__.return_value.submit.return_value = (
            mock_future
        )

        scripts = [{"path": "script1.sas"}, {"path": "script2.sas"}]
        self.runner._execute_scripts(scripts)

        self.comm.complete_signal.emit.assert_called_with("script1.sas: 成功", True)
        self.comm.progress_signal.emit.assert_called_with(1)
        self.assertFalse(self.runner.running)

    @patch("saspy.core.script_runner.ThreadPoolExecutor")
    @patch("saspy.core.script_runner.as_completed")
    def test_execute_scripts_stopped(self, mock_as_completed, mock_executor):
        mock_future = MagicMock()
        mock_future.result.return_value = True
        mock_as_completed.return_value = [mock_future]
        mock_executor.return_value.__enter__.return_value.submit.return_value = (
            mock_future
        )

        scripts = [{"path": "script1.sas"}, {"path": "script2.sas"}]
        self.runner.running = False
        self.runner._execute_scripts(scripts)

        self.comm.complete_signal.emit.assert_not_called()
        self.comm.progress_signal.emit.assert_not_called()


if __name__ == "__main__":
    unittest.main()
