from win32com.client import Dispatch

x = Dispatch("Excel.Application")
x.Visible = True
w = x.Workbooks.Add()
x.Cells(1, 1).Value = "Hello, world!"
