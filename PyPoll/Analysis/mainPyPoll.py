'PyPoll'

import os
import csv

# Set the path for the input file
file_path = "C:/Users/Andrews/OneDrive/UTDataBootcamp/Python-challenge/PyPoll/Resources/election_data.csv"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    header = next(csv_reader)
    
    # Loop through the rows in the CSV file
    for row in csv_reader:
        # Increment the total number of votes
        total_votes += 1
        
        # Get the candidate name from the row
        candidate = row[2]
        
        # If the candidate already exists in the dictionary, increment their vote count
        if candidate in candidates:
            candidates[candidate] += 1
        # Otherwise, add the candidate to the dictionary with an initial vote count of 1
        else:
            candidates[candidate] = 1

# Print the election results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Iterate over the candidates dictionary to calculate and print their percentage of votes
for candidate, votes in candidates.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    
    # Check if the current candidate has the most votes
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
