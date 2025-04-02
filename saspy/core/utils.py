import os
import json
from PyQt5.QtWidgets import QFileDialog, QMessageBox

def select_project_path():
    path = QFileDialog.getExistingDirectory(None, "Select Project Directory")
    return path

def select_sas_executable():
    path, _ = QFileDialog.getOpenFileName(None, "Select SAS Executable", "", "Executable Files (*.exe)")
    return path

def select_sas_config():
    path, _ = QFileDialog.getOpenFileName(None, "Select SAS Config File", "", "Config Files (*.cfg)")
    return path

def save_configuration(config):
    path, _ = QFileDialog.getSaveFileName(None, "保存配置", "", "JSON文件 (*.json)")
    if path:
        with open(path, "w") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

def load_configuration(script_groups):
    path, _ = QFileDialog.getOpenFileName(None, "加载配置", "", "JSON文件 (*.json)")
    if path:
        try:
            with open(path, "r") as f:
                config = json.load(f)
                required_keys = ["project_path", "sas_executable", "sas_config", "scripts"]
                if not all(k in config for k in required_keys):
                    raise ValueError("缺少必要配置字段")

                for cat in script_groups:
                    if cat not in config["scripts"]:
                        raise ValueError(f"缺少分类配置: {cat}")
                    for stype in ["dev", "qc"]:
                        if stype not in config["scripts"][cat]:
                            raise ValueError(f"{cat} 缺少 {stype} 配置")

                return config
        except json.JSONDecodeError as e:
            QMessageBox.critical(None, "加载错误", f"配置加载失败: JSON 解码错误 - {str(e)}")
        except Exception as e:
            QMessageBox.critical(None, "加载错误", f"配置加载失败: {str(e)}")
    return None