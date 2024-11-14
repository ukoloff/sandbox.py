#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX
#
import os
from dbfread import DBF
import pandas

src = r"C:\Paket\Baza\KorStat.dbf"
dst = r"\\kzkserv\Data\Baza_23\stat\stat.xlsx"

if not os.path.isfile(src):
    print("File not found: ", src)
    exit()

data = DBF(src, encoding="cp866")
frame = pandas.DataFrame(iter(data))
frame = frame.convert_dtypes()

prev = 0

if os.path.isfile(dst):
    prev = 1
    load = pandas.read_excel(dst)
    frame = pandas.concat([load, frame], ignore_index=True)
    load = None

frame.to_excel(dst, freeze_panes=(1, 0), index=False, sheet_name='korStat')

if not prev:
    exit()

# Remove duplicates
frame = pandas.read_excel(dst)
frame.drop_duplicates(inplace=True)
frame.to_excel(dst, freeze_panes=(1, 0), index=False, sheet_name='korStat')
