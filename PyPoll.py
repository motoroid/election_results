# Data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each acndidate won
# The winner of the election based on popular vote
# add our depedencies
import csv
import os
# Assign a variable for the file to load and the path
file_to_load= os.path.join("Resources", "election_results.csv")
# create a filename variable to a direct or indirect path to the file. 
file_to_save=os.path.join("analysis", "election_analysis.txt")
#1. initialize a total vote counter
total_votes = 0
#candidate options
candidate_options = []
# create candidate vote dictionary
candidate_votes ={}
#Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



# Open the election results and read the file
with open(file_to_load) as election_data:

   
# Read the file object with the reader function
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
# Print each row in the CSV file
    for row in file_reader:
        #2 Add to the total vote count
        total_votes +=1
       # Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            #begin tracking candidate's votes
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count
        candidate_votes[candidate_name] +=1   
    #determine the percentage of votes for each candidate by looping 
    #through the counts
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate
        votes=candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage=float(votes)/float(total_votes)*100
        #determine winning cote count and candidate
        #determine if the votes is greater than the winning count
        
        #print the candidate name and percentage of votes
        print (f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,})\n")

        if (votes >winning_count) and (vote_percentage>winning_percentage):
            #if true then set winning_count = votes and winning_percent =
            #vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)   
        
        
    




