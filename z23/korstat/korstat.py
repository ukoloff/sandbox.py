#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX
#
import os
import openpyxl
from dbfread import DBF

src = r"C:\Paket\Baza\KorStat.dbf"
dst = r"\\kzkserv\Data\Baza_23\stat\stat.xlsx"

dst = os.path.join(__file__, "../../../tmp/stat.xlsx")

if not os.path.isfile(src):
    print("File not found: ", src)
    exit()

data = DBF(src, encoding="cp866")

wb = openpyxl.Workbook()
ws = wb.active

for row in data:
    ws.append(list(row.values()))

wb.save(dst)
