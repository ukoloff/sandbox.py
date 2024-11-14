#
# Перенос записей из C:\Paket\Baza\KorStat.dbf в \\kzkserv\Data\Baza_23\stat\stat.XLSX`
#
import os
from dbfread import DBF

src = os.path.join(__file__, '../data/KORSTAT_5.DBF')

data = DBF(src, encoding='cp866')
print(*data)
