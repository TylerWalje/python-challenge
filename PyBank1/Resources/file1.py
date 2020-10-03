import os
import csv

file1 = os.path.join("budget_data_csv")

with open(file1, newline = " ")

    csvreader = csv.reader(file1, delimiter = ",")

for row in csvreader

dates.append(row[1])

firstrow = next(csvreader)
totalmonths += 1
totalamount += int(firstrow)
value = int(firstrow)

totalmonths = 0
totalamount = 0
months = []
value = []
dates = []
profit = []

for row in csvreader
    dates.append(row[0])

    change = int(row[1])-value

    value = int(row[1])

greatestincreaseprofits = mac(profit)
#increasedate = dates[greate]????

greatestdecreaseprofits = min)profit)

    #csvreader = csv.reader(csvfile, delimiter=',')

    csv header = next(csvreader)
    print(f"")

   with open(file1, newline= 'r', firstrow= '') as csvfile
    csvreader = csv.reader(csvfile, delimiter=',') 
        for row in csvreader
            if row [0]



profits.append(value)
value = int()

print(Financial Analasys)
print(f"totalmonths: {str[totalmonths]}")
print(f"totalamount: {str[totalamount]}")
print(f"")