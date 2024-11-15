#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX
#
import os
import json
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


if not os.path.isfile(src):
    print("File not found: ", src)
    exit()

wbo = openpyxl.Workbook(write_only=True)
wso = wbo.create_sheet()
wso.title = "korStat"
wso.freeze_panes = "A2"

wbi = openpyxl.load_workbook(dst, read_only=True, data_only=True)
wsi = wbi.active
for row in wsi:
    wso.append([openpyxl.cell.WriteOnlyCell(wso, value=cell.value) for cell in row])
    # print(json.dumps([cell.value for cell in row], ensure_ascii=False, default=json_serial))
wbi.close()

data = DBF(src, encoding="cp866")
first = True
for row in data:
    if first:
        header = []
        font = openpyxl.styles.Font(bold=True)
        align = openpyxl.styles.Alignment(horizontal="center")
        for name in row.keys():
            cell = openpyxl.cell.WriteOnlyCell(wso, value=name)
            cell.font = font
            cell.alignment = align
            header.append(cell)
        wso.append(header)
        first = False
    wso.append(list(row.values()))

wbo.save(dst)
