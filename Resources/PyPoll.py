# The data we need to retrieve.
# Open the election results and read the file
file_to_load = 'election_results.csv'

with open(file_to_load) as election_data:
    print(election_data)

#1.The total number of votes cast
#2.A complete list of candidates who received votes
#3.The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5.The winner of the election based on the popular vote.

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")