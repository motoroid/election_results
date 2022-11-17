# Data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each acndidate won
# The winner of the election based on popular vote
# find our depedencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources", "election_results.csv")
# create a filename variable to a direct or indirect path to the file. 
file_to_save=os.path.join("analysis", "election_analysis.txt")
# Using the with statement to ope instead of the open

# Open the election results and read the file
with open(file_to_load) as election_data:

   
# Read the file object with the reader function
    file_reader = csv.reader(election_data)
# print the header row
    headers=next(file_reader)
    print(headers)