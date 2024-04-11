import csv
import os

# Create variables
votes = 0
candidates = {}
winner = ""
winningvotes = 0

# Csv path
csv_path = os.path.join('PyPoll', 'Resources', 'election_data.csv')