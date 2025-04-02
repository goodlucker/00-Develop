# pdf2com.py
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyPDF2 import PdfReader

def extract_annotations(pdf_path):
    # 打开PDF文件
    pypdf_doc = PdfReader(open(pdf_path, "rb"))
    
    # 遍历所有页面
    for page_num in range(len(pypdf_doc.pages)):
        pypdf_page = pypdf_doc.pages[page_num]
        
        # 检查页面是否包含批注
        if '/Annots' in pypdf_page:
            print(f"Page {page_num + 1} has {len(pypdf_page['/Annots'])} annotations.")
            for annot in pypdf_page['/Annots']:
                annot_obj = annot.get_object()
                subtype = annot_obj.get('/Subtype')
                # 获取批注内容
                contents = annot_obj.get('/Contents', 'No content')
                # 如果内容是bytes，解码为字符串
                if isinstance(contents, bytes):
                    contents = contents.decode('utf-8')
                
                # 打印批注详细信息
                print(f"Page: {page_num + 1}, Type: {subtype}, Content: {contents}")
        else:
            print(f"Page {page_num + 1} has no annotations.")

# 示例：读取并打印批注
pdf_file = r'D:\CRM-L460\D-disk\98_App\Scripts\pdf\test.pdf'  # 使用原始字符串指定PDF文件路径
extract_annotations(pdf_file)
