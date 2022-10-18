# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
from operator import truediv
import os

# Define string variable as directory location
path = "C:\\Users\\bpiet\\OneDrive\\Desktop\\02 - UCF Data Analytics BC\\04 - Module 3_Intro to Python\\02 - Deliverables"


# Add a variable to load a file from a path.
file_to_load = os.path.join(path, "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join(path, "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_name_options = []
county_dict = {}

count = 0
change_count = 0
vote_count = 0
rowcount = 369711

file = open('election_results.csv')
csvreader = csv.reader(file)
rows = list(csvreader)

for row in rows:
    count += 1
    if rowcount > count > 1:
        vote_count += 1
        next_row = rows[count]
        if row[1] != next_row[1]:
            county_dict[row[1]] = vote_count
            vote_count = 0
    elif count == rowcount:
        county_dict[row[1]] = vote_count + 2


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.

county_votes = list(county_dict.values())
sorted_county_votes = sorted(county_votes, reverse=False)
largest_county_vote = sorted_county_votes[len(sorted_county_votes) - 1]
largest_county = list(county_dict.keys())[list(county_dict.values()).index(sorted_county_votes[-1])]


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_name_options:

            # 4b: Add the existing county to the list of counties.
            county_name_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_dict[county_name] = 0

        # 5: Add a vote to that county's vote count.    
        county_dict[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    # print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in list(county_dict.keys()):

        # 6b: Retrieve the county vote count.
        county_vote_count = county_dict[county]

        # 6c: Calculate the percentage of votes for the county.
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
        print(county_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write an if statement to determine the winning county and get its vote count. 
         # Ben -> Already determined the largest county and it's vote count
        if county == largest_county:
            winning_vote_percentage = county_vote_percentage
        
    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
    f"-------------------------\n"
    f"Winner: {largest_county}\n"
    f"Winning Vote Count: {largest_county_vote:,}\n"
    f"Winning Percentage: {winning_vote_percentage:.1f}%\n"
    f"-------------------------\n")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
