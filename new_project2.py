import csv

'''with open('valeursfoncieres-2020 (2).txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(",") for line in stripped if line)
    with open('valeursfoncieres-2020.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        #writer.writerow(('title', 'intro'))
        writer.writerows(lines)

import pandas as pd
df = pd.read_fwf('valeursfoncieres-2020 (2).txt')
df.to_csv('log.csv')

with open('valeursfoncieres-2020 (2).txt', 'r') as infile, open('csvfile', 'w') as outfile:
    stripped = (line.strip() for line in infile)
    lines = (line.split(",") for line in stripped if line)
    writer = csv.writer(outfile)
    writer.writerows(lines)
import csv
'''
with open('valeursfoncieres-2020 (2).txt', 'r') as infile, open('csvfile.csv', 'w') as outfile:
     stripped = (line.strip() for line in infile)
     lines = (line.split(",") for line in stripped if line)
     writer = csv.writer(outfile)
     writer.writerows(lines)
