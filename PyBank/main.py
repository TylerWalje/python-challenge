import csv
import os

# Create variables
months = 0
total = 0
previous = None
monthlychange = []
increase = ['', 0]
decrease = ['', 0]

# csv path
csv_path = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader) 

    for row in csvreader:
 
        months += 1
        total += int(row[1])

        # Monthly change
        if previous is not None:
            change = int(row[1]) - previous
            monthlychange.append(change)

            # Profits increace
            if change > increase[1]:
                increase = [row[0], change]

            # Profits decrease
            if change < decrease[1]:
                decrease = [row[0], change]

        previous = int(row[1])

        # average change
average_change = sum(monthlychange) / len(monthlychange) if monthlychange else 0

# Output
summary = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})"
)

print(summary)

# Output to text file in folder
output_path = 'PyBank/analysis/financial_analysis_summary.txt'
with open(output_path, 'w') as file:
    file.write(summary)
    