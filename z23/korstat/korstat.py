#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX
#
import os
import openpyxl
from dbfread import DBF
import openpyxl.styles

src = r"C:\Paket\Baza\KorStat.dbf"
dst = r"\\kzkserv\Data\Baza_23\stat\stat.xlsx"

dst = os.path.join(__file__, "../../../tmp/stat.xlsx")

if not os.path.isfile(src):
    print("File not found: ", src)
    exit()

data = DBF(src, encoding="cp866")

wb = openpyxl.Workbook()
ws = wb.active

first = True

for row in data:
    if first:
        ws.append(list(row.keys()))
        font = openpyxl.styles.Font(bold=True)
        align = openpyxl.styles.Alignment(horizontal='center')
        for cell in ws[1]:
            cell.font = font
            cell.alignment = align
        ws.freeze_panes = 'A2'
        first = False
    ws.append(list(row.values()))

wb.save(dst)
