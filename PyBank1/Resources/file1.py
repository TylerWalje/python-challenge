import os
import csv

file1 = os.path.join("budget_data_csv")

totalmonths = 0
totalamount = 0
change = 0
value = 0
dates = []
profit = []

with open(file1, newline = " ") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvfile)

for row in csvreader:
#tracking dates
    dates.append(row[0])

    firstrow = next(csvreader)
    totalmonths += 1
    totalamount += int(firstrow)
    value = int(firstrow)


#tracking change
    change = int(row[1])-value

    profit.append(change)

    value = int(row[1])

#total profits (everything)
totalamount = totalamount + int(row[1])

#greatest increase profits
greatestincreaseprofits = max(profit)
greatestincrease = profit.index(greatestincreaseprofits)
increasedate = dates[greatestincrease]

#least growth in profits
greatestdecreaseprofits = min(profit)
greatestdecrease = profit.index(greatestdecreaseprofits)
decreasedate = dates[greatestdecrease]


    csv header = next(csvreader)
    print(f"")

   with open(file1, newline= 'r', firstrow= '') as csvfile
    csvreader = csv.reader(csvfile, delimiter=',') 
        for row in csvreader
            if row [0]



profits.append(value)
value = int()

print(Financial Analasys)
print(f"Total Months: {str[totalmonths]}")
print(f"Total Amount: {str[totalamount]}")
print(f"Average Change: {str(round(")
print (f"Greatest Increase In Profits: {increasedate} {str(greatestincreaseprofits}")
print (f"Greatest Decrease In Profits: {decreasedate} {str(greatestdecreaseprofits}")