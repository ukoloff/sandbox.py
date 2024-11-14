#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX`
#
import os
from dbfread import DBF
from pandas import DataFrame

src = os.path.join(__file__, '../data/KORSTAT_5.DBF')

data = DBF(src, encoding='cp866')
frame = DataFrame(iter(data))
# print(frame)

dst = os.path.join(__file__, '../../../tmp/stat.xlsx')
frame.to_excel(dst)
