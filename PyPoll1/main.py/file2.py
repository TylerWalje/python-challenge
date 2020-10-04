import os
import csv

electionresults = os.path.join("election_data.csv")

#with file()

with open(electionresults, newline - "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:
        #counting total amount of votes and adding to the votes
        totalvotes = 0
        toalvotes += 1

#lists and counters
candidates = []
percentageofvotes = []
votes = 0
totalvotes = 0

if row[] not in candidates
    candidates.append()
    index = candidates.index(row[])
    num.votes.append(1)
else:
    pass candidates.append()
    num.votes[index] += 1

#printing the info
print("Election Results")
print("Total Votes: {}")