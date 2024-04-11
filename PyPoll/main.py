import csv
import os

# Create variables
votes = 0
candidates = {}

# Csv path
csv_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')

with open(csv_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  

    for row in csvreader:
        votes += 1 
        candidate_name = row[2] 

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1


# Output to text file in folder
# pathout = os.path.join('PyPoll', 'analysis', 'election_results_summary.txt')
# with open(pathout, 'w') as file:
   # file.write(summary)