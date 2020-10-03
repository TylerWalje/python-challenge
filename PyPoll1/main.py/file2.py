import os
import csv

electionresults = os.path.join("election_data.csv")

with open(electionresults, newline - "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader)

    for row in csvreader:
        #counting total amount of votes and adding to the votes
        totalvotes = 0
        toalvotes += 1

candidates = []
percentageofvotes = 0
votes = 0
totalvotes = 0

