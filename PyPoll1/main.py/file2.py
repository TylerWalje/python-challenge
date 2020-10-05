import os
import csv

electionresults = os.path.join("election_data.csv")


#lists and counters
candidates = []
percentageofvotes = []
votes = []
totalvotes = 0

#with file()

with open(electionresults, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)
    for row in csvreader:

        #counting total amount of votes and adding to the votes
        totalvotes += 1

#look for names, add names and add votes
if row[2] not in candidates:
    candidates.append(row[2])
    index = candidates.index(row[2])
    votes.append(1)
else:
    index = candidates.append(row[2])
    votes[index] += 1

for votes1 in votes:
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
print(f"Total Votes: {str(totalvotes)}")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percentageofvotes[i])} ({str(votes[i])})")
print(f"Winner: {electionwinner}")



#export solution
solution = open("solution.txt", "w")

line1 = "Election Results"
line2 = str(f"Total Votes: {str(totalvotes)}")
line3 = "____"
solution.write('{}\n{}\n{}\n'.format(line1, line2, line3)) 
for i in range(len(candidates)):
    line = str(f"{candidates[i]}: {str(percentageofvotes[i])} ({str(votes[i])})")
    solution.write('{}\n'.format(line))
line4 = str(f"Winner: {electionwinner}")
solution.write('{}\n'.format(line4))