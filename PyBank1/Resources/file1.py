import os
import csv

file = os.path.join("budget_data_csv")

with open(file, 'r') as text:

    print(text)

    lines - text.read()

    print (lines)

with open(csvpath, newline= '') as csvfile

    csvreader = csv.reader(csvfile, delimiter=',')

    csv header = next(csvreader)
