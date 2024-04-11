import csv

# Create variables
months = 0
total = 0
previous = None
monthlychange = []
increase = ['', 0]
decrease = ['', 0]

# csv path
csv_path = 'PyBank/Resources/budget_data.csv'

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