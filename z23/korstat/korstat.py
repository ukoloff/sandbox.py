#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX`
#
import os
from dbfread import DBF
import pandas
# import DataFrame

src = os.path.join(__file__, "../data/KORSTAT_5.DBF")

data = DBF(src, encoding="cp866")
frame = pandas.DataFrame(iter(data))

dst = os.path.join(__file__, "../../../tmp/stat.xlsx")
if os.path.isfile(dst):
    load = pandas.read_excel(dst)
frame.to_excel(dst, freeze_panes=(1, 0), index=False)
