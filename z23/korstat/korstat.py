#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX
#
import os
import json
import hashlib
from datetime import date, datetime
import openpyxl
from dbfread import DBF
import openpyxl.cell
import openpyxl.styles

src = r"C:\Paket\Baza\KorStat.dbf"
dst = r"\\kzkserv\Data\Baza_23\stat\stat.xlsx"

dst = os.path.join(__file__, "../../../tmp/stat.xlsx")


# https://stackoverflow.com/a/22238613/6127481
def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type %s not serializable" % type(obj))


def hash(data):
    return hashlib.sha256(
        json.dumps(data, ensure_ascii=False, default=json_serial)
    ).hexdigest()


if not os.path.isfile(src):
    print("File not found: ", src)
    exit()

wbo = openpyxl.Workbook(write_only=True)
wso = wbo.create_sheet()
wso.title = "korStat"
wso.freeze_panes = "A2"


def add(data, header=False):
    if not header:
        wso.append(data)
        return
    row = []
    font = openpyxl.styles.Font(bold=True)
    align = openpyxl.styles.Alignment(horizontal="center")
    for it in data:
        cell = openpyxl.cell.WriteOnlyCell(wso, value=it)
        cell.font = font
        cell.alignment = align
        row.append(cell)
    wso.append(row)

first = True
if os.path.isfile(dst):
  wbi = openpyxl.load_workbook(dst, read_only=True, data_only=True)
  wsi = wbi.active
  for row in wsi:
      data = [cell.value for cell in row]
      add(data, first)
      first = False
  wbi.close()

data = DBF(src, encoding="cp866")
for row in data:
    if first:
        add(list(row.keys()), first)
        first = False
    row = list(row.values())
    add(row)

wbo.save(dst)
