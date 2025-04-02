#查找当前目录下的全部word文件
import os
import glob
from pathlib import Path
from docx2pdf import convert


path = os.getcwd() + '/'
p = Path(path) #初始化构造Path对象
FileList=list(p.glob("**/*.docx")) 

for file in FileList:
    convert(file,f"{file}.pdf")
