from pathlib import Path

import comtypes.client

word = comtypes.client.CreateObject('Word.Application')
doc = word.Documents.Open(str(Path('TestDocument.doc').absolute()))
wdFormatPDF = 17
doc.SaveAs(str(Path('1.pdf').absolute()), FileFormat=wdFormatPDF)
doc.Close()
word.Quit()