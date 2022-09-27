# Election_Analysis

## Project Overview
A colorado Board of Elections employee has tasked me with completing an election audit of a recent  congressional election. The tasks that were requested are as follows:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. The voter turnout for each county.
7. The percentage of votes from each county out of the toal count of votes.
8. The county with the highest turn out.

## Resources
- Data Sources: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The counties involved in this election audit were:
    - Denver
    - Jefferson
    - Arapahoe
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The voter turnout for each county is as follows
    - Jefferson county had 10.5% of the votes (38,855 total votes).
    - Denver had 82.8% of the votes (306,055 total votes).
    - Arapahoe had 6.7% of the votes (24,801 total votes)
- The county with the highest voter turnout was Denver!

- **The winner of the election was Diana DeGette, who receieved 73.8% of the vote and 272,892 number of votes!!!**
    
![Winner_screenshot](https://user-images.githubusercontent.com/112278208/192608449-79d2b3bb-dc54-4486-8dc0-712cd4c71328.png)


The raw data to the election results can be found here: [Election Results](https://github.com/Kcav18/Election_Analysis/blob/main/Resources/election_results.csv)

The text file summary of the election results can be found here: [Election Analysis](https://github.com/Kcav18/Election_Analysis/blob/main/analysis/election_analysis.txt)

##  Election Audit Summary

The script to complete this particular election audit is shown below:

```
# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.

county_list = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
winning_county = ""
winningcounty_count=0
winning_county_percentage=0

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
        county_name=row[1]

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
        if county_name not in county_list:

            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name]+=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:

        # 6b: Retrieve the county vote count.
        countyvotes=county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        countyvotes_percentage = float(countyvotes)/float(total_votes)*100

         # 6d: Print the county results to the terminal.
        print(f"{county_name}: {countyvotes_percentage:.1f}% ({countyvotes:,})")
         # 6e: Save the county votes to a text file.
        county_election_results= (f"{county_name}: {countyvotes_percentage:.1f}% ({countyvotes:,})\n")
        txt_file.write(county_election_results)

         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (countyvotes>winningcounty_count) and (countyvotes>winning_county_percentage):
            winningcounty_count=countyvotes
            winning_county=county_name
            winning_county_percentage=countyvotes_percentage

    # 7: Print the county with the largest turnout to the terminal.
        winning_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")

    print(winning_county_summary, end="")

    # 8: Save the county with the largest turnout to a text file.
    county_turnout = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n")
    txt_file.write(county_turnout)

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


```


This code could easily be modified to  audit other congressional districts, senatorial districts, and other local elections. It can be used on any data file regardless of the size so long as the dataset has a similar structure.

The bullets below show a couple of examples of how this code can be modified by the election commission for other use:

- This code could be updated to show the election commission which candidate won in each county and not just the overall winner. This would show which candidate is favored in each county.

- Modification of this code could also showcase which candidate won the most counties in Colorado- which may be different than the overall popular vote. 


