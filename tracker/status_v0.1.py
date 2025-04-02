#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Rick.Xu

import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import string
import logging

# 设置日志记录配置
logging.basicConfig(level=logging.DEBUG, filename='debug.log', filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s')

CONFIG_FILE = 'config.json'

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
    input_file_var.set(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    output_file_var.set(file_path)

def column_letter_to_index(letter):
    return string.ascii_uppercase.index(letter.upper()) + 1

def generate_report():
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    sheet_names = sheet_name_var.get().split(',')
    column_letters = column_name_var.get().split('@')
    header_row = int(header_row_var.get())

    if not input_file or not output_file or not sheet_name_var.get() or not column_name_var.get() or header_row <= 0:
        messagebox.showerror("Error", "请填写所有字段，并确认行号大于0")
        return

    try:
        wb = Workbook()
        
        for sheet_name in sheet_names:
            try:
                df = pd.read_excel(input_file, sheet_name=sheet_name.strip(), header=header_row - 1)
                logging.debug(f"DataFrame for sheet '{sheet_name.strip()}' loaded successfully. DataFrame head:\n{df.head()}")
            except Exception as e:
                logging.error(f"读取输入文件的Sheet '{sheet_name.strip()}'时发生错误", exc_info=True)
                messagebox.showerror("Error", f"读取输入文件的Sheet '{sheet_name.strip()}'时发生错误，请检查日志文件以获取详细信息")
                continue

            ws = wb.create_sheet(title=sheet_name.strip())

            for columns in column_letters:
                letters = [col.strip() for col in columns.split(',')]
                col_names = [df.columns[column_letter_to_index(letter) - 1] for letter in letters]
                logging.debug(f"Processing columns in sheet '{sheet_name.strip()}': {col_names}")

                if len(col_names) < 2:
                    messagebox.showerror("Error", f"每组列名中至少应该包含两个列名: {columns}")
                    return

                # 计算交叉频数
                try:
                    frequency = pd.crosstab(index=[df[col] for col in col_names[:-1]], columns=df[col_names[-1]], dropna=False)
                    frequency = frequency.reset_index()
                    logging.debug(f"Cross-tabulated data for sheet '{sheet_name.strip()}':\n{frequency.head()}")
                except Exception as e:
                    logging.error(f"Error in computing crosstab for columns {col_names} in sheet '{sheet_name.strip()}'", exc_info=True)
                    messagebox.showerror("Error", f"计算交叉频数时发生错误，请检查日志文件以获取详细信息")
                    return

                # 构建表头
                try:
                    sheet_title = "与".join(col_names) + " 的交叉频数"
                    ws.append([sheet_title])

                    # 导出索引和列名
                    headers = list(frequency.columns)
                    index_columns = col_names[:-1]
                    final_headers = index_columns + headers[1:]  # headers[1:] to avoid duplication of the first column
                    logging.debug(f"Headers for Excel in sheet '{sheet_name.strip()}': {final_headers}")
                    ws.append(final_headers)

                    for row in dataframe_to_rows(frequency, index=False, header=False):
                        ws.append(row)

                    ws.append([])  # 添加空行以分隔不同组的统计结果
                except Exception as e:
                    logging.error(f"Error in writing data to Excel for columns {col_names} in sheet '{sheet_name.strip()}'", exc_info=True)
                    messagebox.showerror("Error", f"写入数据到Excel时发生错误，请检查日志文件以获取详细信息")
                    return

        wb.save(output_file)
        messagebox.showinfo("Success", f"统计结果已保存到 {output_file}")
    except Exception as e:
        logging.error("生成报告时发生错误", exc_info=True)
        messagebox.showerror("Error", "生成报告时发生错误，请检查日志文件以获取详细信息")

def save_configuration():
    config = {
        "input_file": input_file_var.get(),
        "output_file": output_file_var.get(),
        "sheet_name": sheet_name_var.get(),
        "column_name": column_name_var.get(),
        "header_row": header_row_var.get()
    }

    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

    messagebox.showinfo("Success", "配置已保存")

def load_configuration():
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            input_file_var.set(config.get("input_file", ""))
            output_file_var.set(config.get("output_file", ""))
            sheet_name_var.set(config.get("sheet_name", ""))
            column_name_var.set(config.get("column_name", ""))
            header_row_var.set(config.get("header_row", 1))
        messagebox.showinfo("Success", "配置已加载")
    except FileNotFoundError:
        pass  # 如果配置文件不存在，就跳过

app = tk.Tk()
app.title("Excel 报告生成器")

input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
sheet_name_var = tk.StringVar()
column_name_var = tk.StringVar()
header_row_var = tk.StringVar(value='1')  # 默认为第1行

# 加载配置
load_configuration()

# UI 设计
tk.Label(app, text="输入文件:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=input_file_var, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(app, text="选择文件", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(app, text="输出文件:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=output_file_var, width=40).grid(row=1, column=1, padx=10, pady=10)
tk.Button(app, text="选择文件", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

tk.Label(app, text="Sheet 名称 (用 , 分隔):").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=sheet_name_var, width=40).grid(row=2, column=1, padx=10, pady=10)

tk.Label(app, text="列号 (用 @ 分隔不同组):").grid(row=3, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=column_name_var, width=40).grid(row=3, column=1, padx=10, pady=10)

tk.Label(app, text="列名起始行号:").grid(row=4, column=0, padx=10, pady=10)
tk.Entry(app, textvariable=header_row_var, width=40).grid(row=4, column=1, padx=10, pady=10)

tk.Button(app, text="生成报告", command=generate_report).grid(row=5, column=0, columnspan=3, pady=5)
tk.Button(app, text="保存配置", command=save_configuration).grid(row=6, column=0, columnspan=3, pady=5)
tk.Button(app, text="加载配置", command=load_configuration).grid(row=7, column=0, columnspan=3, pady=5)

app.mainloop()