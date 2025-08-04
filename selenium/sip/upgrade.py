#
# Обновление списков FreePBX
#
import csv
from os.path import join, dirname


def readCSV():
    src = join(dirname(__file__), "data", "omz2sinara.csv")
    with open(src) as f:
        reader = csv.DictReader(f, delimiter=";")
        return dict((row["extension"], row) for row in reader)


extensions = readCSV()
print(extensions)
