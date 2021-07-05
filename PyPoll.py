## To Do List
#  1. Total number of votes cast
#  2. A complete list of candidates who received votes
#  3. Total number of votes each candidate received
#  4. Percentage of votes each candidate won
#  5. The winner of the election based on popular vote
# Election results file located in this repository at: Resources\election_results.csv

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
#print("The time right now is ", now)
### ---------------------------------------------------------------------------
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1a. Initialize a total vote counter.
total_votes = 0
# 2a. Candidate Options
candidate_options = []
# 3a. Declare the empty dictionary.
candidate_votes = {}
# 5a. Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
    #    print(row)
# 1b. Add to the total vote count.
        total_votes += 1
        # 1c. Print the total votes.
#print(total_votes)
        # 2b. Print the candidate name from each row.
        candidate_name = row[2]
        # 2c.  If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
        # 2d.Add candidate name to the list of candidates.
            candidate_options.append(candidate_name)
        # 3b. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # 3c. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
        #2 Print the candidate list.
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #print(candidate_options)
    # Print the candidate vote dictionary.
    #print(candidate_votes)
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 4a.. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 4b. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 4c. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    #  5b. print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # 5c. Determine winning vote count and candidate
        # 5d. Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 5e. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 5f. And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    # 5g. Print Results
    #print(winning_candidate_summary)
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)