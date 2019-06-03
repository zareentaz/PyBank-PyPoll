import os
import csv
PyPoll = "election_data.csv"
TotalVotes = 0
Total_Rows=0
candidate_names=[]

# read number of rows inclusing header
with open(PyPoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    Total_Rows=sum(1 for line in csvfile)
    # Total_Rows - 1 = TotalVotes
    TotalVotes = (Total_Rows - 1)
    # print Total votes
    print(f"Total votes: {TotalVotes}")

with open(PyPoll) as csvfile:
    csv_header = next(csvfile)
    for row in csvfile:
        name = row.split(",")[2]
        if name not in candidate_names:
            candidate_names.append(name)
            print(name)


#with open(PyPoll, newline="", encoding="utf-8")as csvfile:
   
    #print(f"Header: {csv_header}")
    #for row in csvreader:
    #    Totalvotes.append(int(row[0]))
#Total=sum(Totalvotes)
#rint(f"Total votes: {Total}")
