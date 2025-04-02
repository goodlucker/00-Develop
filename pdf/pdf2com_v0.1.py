# pdf2com.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def extract_bookmarks(reader):
    """提取PDF中的书签，返回页面号与书签名称的字典"""
    bookmarks = {}

    def _parse_bookmark(outline, parent_title=''):
        if isinstance(outline, list):
            for item in outline:
                _parse_bookmark(item, parent_title)
        else:
            title = f"{parent_title} > {outline.title}" if parent_title else outline.title
            try:
                page_num = reader.get_destination_page_number(outline)
                bookmarks[page_num] = title
            except Exception as e:
                print(f"Error parsing bookmark: {e}")

    outlines = reader.outline  # 使用 outline 属性来获取书签
    _parse_bookmark(outlines)

    return bookmarks

def extract_annotations(pdf_path):
    # 打开PDF文件
    pypdf_doc = PdfReader(open(pdf_path, "rb"))
    annotations = []

    # 获取书签
    bookmarks = extract_bookmarks(pypdf_doc)

    # 遍历所有页面
    for page_num in range(len(pypdf_doc.pages)):
        pypdf_page = pypdf_doc.pages[page_num]
        bookmark_name = bookmarks.get(page_num, "No Bookmark")

        # 检查页面是否包含批注
        if '/Annots' in pypdf_page:
            rect_annotations = {}
            
            for annot in pypdf_page['/Annots']:
                annot_obj = annot.get_object()
                subtype = annot_obj.get('/Subtype')
                contents = annot_obj.get('/Contents', 'No content')
                rect = tuple(annot_obj.get('/Rect'))
                author = annot_obj.get('/T', 'Unknown author')
                
                # 如果内容是bytes，解码为字符串
                if isinstance(contents, bytes):
                    contents = contents.decode('utf-8')
                if isinstance(author, bytes):
                    author = author.decode('utf-8')

                # 按Rect存储批注，以便关联批注和回复
                if rect not in rect_annotations:
                    rect_annotations[rect] = []
                
                rect_annotations[rect].append({
                    "Page": page_num + 1,
                    "Bookmark": bookmark_name,
                    "Annotation Type": subtype,
                    "Content": contents,
                    "Author": author,
                    "Rect": rect
                })

            # 将同一Rect的批注和回复分开存储
            for rect, comments in rect_annotations.items():
                base_comment = comments[0]  # 第一条批注
                other_comments = comments[1:]  # 后续批注（可能是回复）
                
                annotation_entry = {
                    "Page": base_comment["Page"],
                    "Bookmark": base_comment["Bookmark"],
                    "Annotation Type": base_comment["Annotation Type"],
                    "Main Comment": base_comment["Content"],
                    "Main Author": base_comment["Author"]
                }

                # 将其他批注内容和作者分别放入不同的列
                for i, reply in enumerate(other_comments, start=1):
                    annotation_entry[f"Reply {i}"] = reply["Content"]
                    annotation_entry[f"Reply {i} Author"] = reply["Author"]

                annotations.append(annotation_entry)

    return annotations

def save_annotations_to_excel(annotations, output_path):
    # 将批注列表转换为DataFrame
    df = pd.DataFrame(annotations)
    # 保存为Excel文件
    df.to_excel(output_path, index=False)

def browse_pdf_file():
    pdf_file.set(filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))

def browse_output_excel():
    output_excel.set(filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")]))

def process_pdf():
    pdf_path = pdf_file.get()
    output_path = output_excel.get()

    if not pdf_path or not output_path:
        messagebox.showwarning("Input Error", "Please select both PDF file and output Excel file.")
        return

    try:
        annotations = extract_annotations(pdf_path)
        save_annotations_to_excel(annotations, output_path)
        messagebox.showinfo("Success", f"Annotations have been saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Processing Error", f"An error occurred: {str(e)}")

# 创建主窗口
root = tk.Tk()
root.title("PDF Annotation Extractor")

# 创建变量来存储文件路径
pdf_file = tk.StringVar()
output_excel = tk.StringVar()

# 创建和布局控件
tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=pdf_file, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_pdf_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select Output Excel File:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(root, textvariable=output_excel, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_output_excel).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Extract Annotations", command=process_pdf).grid(row=2, columnspan=3, pady=20)

# 运行主循环
root.mainloop()
