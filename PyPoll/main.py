import os
import csv

csvpath = os.path.join('Resources','election_data.csv')

# lists to store data (week 3 part 2 assignment 12)
can_votes = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
# add can_votes
        can_votes.append(row[2])

# python script that analyzes the data

# total number of votes case
total_votes = len(can_votes)

# complete list of candidates who recieved votes
set(can_votes)
# print(set(can_votes)) to see all the candidate names who got votes

# total number of votes each candidate won
stockham_votes = can_votes.count("Charles Casper Stockham")

degette_votes = can_votes.count("Diana DeGette")

doane_votes = can_votes.count('Raymon Anthony Doane')

# percentage of votes each candidate won
stockham_percent = stockham_votes / total_votes
spercentage = f"{stockham_percent:.2%}"

degette_percent = degette_votes / total_votes
dpercentage = f"{degette_percent:.2%}"

doane_percent = doane_votes / total_votes
dopercentage = f"{doane_percent:.2%}"

# Printed Analysis
print("Election Results")
print()
print("-"*40)
print()
print("Total Votes: " + str(total_votes))
print()
print("-"*40)
print()
print("Charles Casper Stockham: " + str(spercentage) + " (" + str(stockham_votes) +")")
print()
print("Diana Degette: " + str(dpercentage) + " (" + str(degette_votes) +")")
print()
print("Raymon Anthony Doane: " + str(dopercentage) + " (" + str(doane_votes) +")")
print()
print("-"*40)
print()
print("Winner: Diana DeGette")
print()
print("-"*40)

# double check answers - Total votes 369711, Charles Casper Stockham: 23.049% (85213),
# Diana DeGette: 73.12% (272892), Raymon Anthony Doane: 3.139% (11606)  Winner: Diana DeGette

#set variable for output file
output_file = os.path.join("election_results.txt")

#open a text file in write mode
with open(output_file, "w") as file:

    #write the results to the text file (total votes, each candidate total votes and percent of votes, winner)
    file.write("Election Results\n")
    file.write("---------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("Charles Casper Stockham: " + str(spercentage) + " (" + str(stockham_votes) +")" + "\n")
    file.write("Diana Degette: " + str(dpercentage) + " (" + str(degette_votes) +")" +"\n")
    file.write("Raymon Anthony Doane: " + str(dopercentage) + " (" + str(doane_votes) +")" + "\n")
    file.write("----------------------------\n")
    file.write("Winner: Diana DeGette")