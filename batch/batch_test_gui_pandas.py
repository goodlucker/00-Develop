import os
import subprocess
import pandas as pd
from tkinter import Tk, filedialog, Button, Label, Entry, Text, Scrollbar, messagebox

# 定义是否单独执行每个 SAS 文件
single_batch = False

# SAS 安装路径和版本配置文件路径
sas_path = r"C:\Program Files\SASHome\SASFoundation\9.4\sas.exe"
sas_ver = r"C:\Program Files\SASHome\SASFoundation\9.4\nls\u8\sasv9.cfg"
sas_user_path = r"C:\Program Files\SASHome\SASFoundation\9.4"

def select_tracker():
    # 选择 Tracker 文件
    track_name = filedialog.askopenfilename(title="Please select the tracker.", filetypes=[("Excel Files", "*.xlsx")])
    if track_name:
        entry_tracker.delete(0, 'end')
        entry_tracker.insert(0, track_name)

def select_sas_files():
    # 选择 SAS 文件
    sas_files = filedialog.askopenfilenames(title="Please select the SAS files.", filetypes=[("SAS Files", "*.sas")])
    if sas_files:
        entry_sas_files.delete(0, 'end')
        entry_sas_files.insert(0, ";".join(sas_files))

def run_batch():
    track_name = entry_tracker.get()
    sas_files = entry_sas_files.get().split(";")
    
    if not track_name or not sas_files:
        messagebox.showerror("Error", "Please select both tracker and SAS files.")
        return

    # 创建 Tkinter 窗口用于显示日志信息
    log_window = Tk()
    log_window.title("Run Log")

    # 创建 Text 控件用于显示日志信息
    log_text = Text(log_window, height=20, width=80)
    log_text.pack(side="left", fill="both", padx=5, pady=5)

    # 创建滚动条
    scrollbar = Scrollbar(log_window, command=log_text.yview)
    scrollbar.pack(side="right", fill="y")
    log_text.config(yscrollcommand=scrollbar.set)

    # 读取 Tracker 文件
    try:
        df = pd.read_excel(track_name, sheet_name="TLFS")
    except Exception as e:
        messagebox.showerror("Error", f"Error reading tracker file: {e}")
        return

    # 获取最大层级
    max_level = df['R'].max()

    # 遍历层级并运行 SAS 程序
    for i in range(1, max_level + 5):
        for sas_file in sas_files:
            file_name = os.path.basename(sas_file)
            level = df.loc[df['R'] == file_name, 'R'].iloc[0]

            if level == i or (i > max_level and (file_name.upper() == "COMPRPT.SAS" or file_name.upper() == "LOGCHK.SAS")):
                log_text.insert("end", f"Running {sas_file}...\n")
                log_text.update()  # 更新日志信息显示
                if single_batch:
                    process = subprocess.Popen([sas_path, "-sysin", sas_file, "-config", sas_ver, "-SASUSER", sas_user_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    stdout, stderr = process.communicate()
                    log_text.insert("end", stdout.decode())
                    log_text.insert("end", stderr.decode())
                else:
                    subprocess.Popen([sas_path, "-sysin", sas_file, "-config", sas_ver, "-SASUSER", sas_user_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    messagebox.showinfo("Complete", f"{len(sas_files)} files complete.")

# 创建 Tkinter 窗口
root = Tk()
root.title("Batch Runner")

# Tracker 文件路径 Entry 和选择按钮
label_tracker = Label(root, text="Tracker File:")
label_tracker.grid(row=0, column=0, padx=5, pady=5)
entry_tracker = Entry(root, width=50)
entry_tracker.grid(row=0, column=1, padx=5, pady=5)
button_select_tracker = Button(root, text="Select", command=select_tracker)
button_select_tracker.grid(row=0, column=2, padx=5, pady=5)

# SAS 文件路径 Entry 和选择按钮
label_sas_files = Label(root, text="SAS Files:")
label_sas_files.grid(row=1, column=0, padx=5, pady=5)
entry_sas_files = Entry(root, width=50)
entry_sas_files.grid(row=1, column=1, padx=5, pady=5)
button_select_sas_files = Button(root, text="Select", command=select_sas_files)
button_select_sas_files.grid(row=1, column=2, padx=5, pady=5)

# 运行按钮
button_run = Button(root, text="Run Batch", command=run_batch)
button_run.grid(row=2, column=1, padx=5, pady=20)

root.mainloop()
