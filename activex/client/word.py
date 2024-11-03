from win32com.client import Dispatch

w = Dispatch("Word.Application")
w.Visible = True
w.Documents.Add()
s = w.Selection
s.TypeText("Hello, world!")
