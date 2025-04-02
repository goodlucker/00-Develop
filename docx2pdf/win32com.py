import os
import win32com.client

wdFormatPDF = 17

inputFile = os.path.abspath("TestDocument.doc")
outputFile = os.path.abspath("document.pdf")
file = open(outputFile, "w")
file.close()
word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(inputFile)
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()