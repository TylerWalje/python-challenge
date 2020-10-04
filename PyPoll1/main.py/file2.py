import os
import csv

electionresults = os.path.join("election_data.csv")

#with file()

with open(electionresults, newline - "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:
        #counting total amount of votes and adding to the votes
        toalvotes += 1

#lists and counters
candidates = []
percentageofvotes = []
votes = 0
totalvotes = 0

#look for names, add names and add votes
if row[2] not in candidates
    candidates.append(row[2])
    index = candidates.index(row[2])
    num.votes.append(1)
else:
    index = candidates.append(row[2])
    num.votes[index] += 1

for votes1 in votes
    percent = (votes1/totalvotes) *100
    percent = round(percent)
    percent = "%.3f%%" % percent
    percentageofvotes.append(percent)

#election winner
winner = max(votes)
index = votes.index(winner)
electionwinner = candidates[index]


#printing the info
print("Election Results")
print("Total Votes: {}")
print