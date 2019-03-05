import os
import csv
import collections

from collections import Counter

electionData = ("election_data.csv")
votes = []
candidates = []
unqiqueCandidates = []
c = Counter()

with open(electionData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

    for candidate in candidates:
        if candidate not in unqiqueCandidates:
            unqiqueCandidates.append(candidate)

   
    c.update(candidates)
winner = max(c, key=c.get)
#couldn't figure out how to use my count dictionary to create the averages per candidate
#meaning, how to extract the vote count to divide by total vote count & repopulate in new dict.

votes_total = len(votes)
print("The total number of votes cast were: " + str(votes_total))
print("The list of candidates is: " + str(unqiqueCandidates))
print(c)
print("The winner is:")
print (winner, c[winner])

filepath =("output.txt")
with open(filepath,'w') as text:
    text.write("Election Results" + "\n")
    text.write("___________________________" + "\n")
    text.write("The total number of votes cast were: " + str(votes_total) + "\n")
    text.write("The list of candidates is: " + str(unqiqueCandidates) + "\n")
    text.write(str(c) + "\n")
    #can't figure out how to export the winner in text
