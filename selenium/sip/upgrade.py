#
# Обновление списков FreePBX
#
import re
import csv
from os.path import join, dirname

data = join(dirname(__file__), "data")


def readCSV():
    src = join(data, "omz2sinara.csv")
    with open(src) as f:
        reader = csv.DictReader(f, delimiter=";")
        return dict((row["extension"], row) for row in reader)

def did(file='dids'):
    with open(join(data, f"{file}.csv"), encoding='utf-8') as f:
        did = [*csv.DictReader(f)]
    with open(join(data, f"{file}.sinara.csv"), 'w', newline='', encoding='utf-8') as f:
      writer = csv.DictWriter(f, fieldnames=[*did[0].keys()])
      writer.writeheader()
      for z in did:
          pfx, ext, tail = z['destination'].split(',', 2)
          if ext not in extensions:
              continue
          z['destination'] = ','.join([pfx, extensions[ext]['extension new'], tail])
          writer.writerow(z)

def exts(file='extensions'):
    with open(join(data, f"{file}.csv"), encoding='utf-8') as f:
        exts = [*csv.DictReader(f)]
    with open(join(data, f"{file}.sinara.csv"), 'w', newline='', encoding='utf-8') as f:
      writer = csv.DictWriter(f, fieldnames=[*exts[0].keys()])
      writer.writeheader()
      for z in exts:
          x = z['extension']
          if x not in extensions:
              continue
          xdata = extensions[x]
          x5 = xdata['extension new']
          for k, v in z.items():
              v5 = re.sub(r'\b' + re.escape(x) + r'\b', x5, v)
              if v5 != v:
                  z[k] = v5
          writer.writerow(z)

extensions = readCSV()

print("Upgrading DIDs...")
did()

print("Upgrading extensions...")
exts()
