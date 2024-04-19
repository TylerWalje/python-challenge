import csv
import os

# Create variables
votes = 0
candidates = {}

os.chdir(os.path.dirname(os.path.realpath(__file__)))
csv_path = os.path.join('Resources', 'election_data.csv')

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

# Election winner
winner = max(candidates, key=candidates.get)

# Output file path
pathout = os.path.join('Analysis', 'election_results_summary.txt')

with open(pathout, 'w') as file:

    print("Election Results")
    print("-------------------")
    print(f"Total Votes: {votes}")
    print("-------------------")
    file.write("Election Results\n")
    file.write("-------------------\n")
    file.write(f"Total Votes: {votes}\n")
    file.write("-------------------\n")

    for candidate, vote_count in candidates.items():
        vote_percentage = (vote_count / votes) * 100
        print(f"{candidate}: {vote_percentage:.3f}% ({vote_count})")
        file.write(f"{candidate}: {vote_percentage:.3f}% ({vote_count})\n")

# Print the results
    print("-------------------")
    print(f"Winner: {winner}")
    print("--------------------")
    file.write("-------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("--------------------\n")
