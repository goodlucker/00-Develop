# word2com.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
import docx
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_comments_from_docx(docx_path):
    doc = docx.Document(docx_path)
    comments = []
    comment_map = {comment.id: comment for comment in doc.part.element.xpath('//w:comment')}

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            comment_start_ids = run._element.xpath('.//w:commentRangeStart/@w:id')
            for comment_id in comment_start_ids:
                comment = comment_map.get(comment_id)
                if comment is not None:
                    comments.append({
                        "Paragraph": paragraph.text.strip(),
                        "Comment": comment.get('w:val'),
                        "Author": comment.get('w:author')
                    })
    return comments

def save_comments_to_excel(comments, output_path):
    df = pd.DataFrame(comments)
    df.to_excel(output_path, index=False)

def browse_word_file():
    word_file.set(filedialog.askopenfilename(filetypes=[("Word files", "*.docx")]))

def browse_output_excel():
    output_excel.set(filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]))

def process_word():
    word_path = word_file.get()
    output_path = output_excel.get()

    if not word_path or not output_path:
        messagebox.showwarning("Input Error", "Please select both Word file and output Excel file.")
        return

    try:
        comments = extract_comments_from_docx(word_path)
        save_comments_to_excel(comments, output_path)
        messagebox.showinfo("Success", f"Comments have been saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Processing Error", f"An error occurred: {str(e)}")

# 创建主窗口
root = tk.Tk()
root.title("Word Comment Extractor")

# 创建变量来存储文件路径
word_file = tk.StringVar()
output_excel = tk.StringVar()

# 创建和布局控件
tk.Label(root, text="Select Word File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=word_file, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_word_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select Output Excel File:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=output_excel, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_excel).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Extract Comments", command=process_word).grid(row=2, columnspan=3, pady=20)

# 运行主循环
root.mainloop()
