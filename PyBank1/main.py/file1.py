import os
import csv

file1 = os.path.join("budget_data.csv")

totalmonths = 0
totalamount = 0
change = 0
value = 0
dates = []
profit = []

with open(file1, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:
#tracking dates
        dates.append(row[0])

        firstrow = next(csvreader)
        totalmonths += 1
        totalamount += int(firstrow[1])
        value = int(firstrow[1])

#header row
    #csvheader = next(csvreader)
    print(f"")
#tracking change
    change = int(row[1])-value

    profit.append(change)

    value = int(row[1])

    totalmonths += 1

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


   #with open(file1, newline= 'r', firstrow= '') as csvfile
    #csvreader = csv.reader(csvfile, delimiter=',') 
        #for row in csvreader
            #if row [0]

change1 = sum(profit)/len(profit)

profit.append(value)
value = int()

print("Financial Analysis")
print(f"Total Months: {str(totalmonths)}")
print(f"Total Amount: ${str(totalamount)}")
print(f"Average Change: ${str(round(change1))}")
print(f"Greatest Increase In Profits: {increasedate} ${str(greatestincreaseprofits)})")
print(f"Greatest Decrease In Profits: {decreasedate} ${str(greatestdecreaseprofits)})")

solution = open("solution.txt", "w")

line1 = "Financial Analysis"
line2 = str(f"Total Months: {str(totalmonths)}")
line3 = str(f"Total: Amount: ${str(totalamount)}")
line4 = str(f"Average Change: ${str(round(change1))}")
line5 = str(f"Greatest Increase in Profits: {greatestincrease} ${str(greatestincreaseprofits)})")
line6 = str(f"Greatest Decrease in Profits: {decreasedate} ${str(greatestdecreaseprofits)})")

solution.write('{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6))