import os
import csv
PyPoll = "election_data.csv"
TotalVotes = 0
Total_Rows=0
candidate_names=[]
election_result={}

print("Election Results")
print("-------------------------")
file1=open("output.txt","w")
file1.write("Election Results")
file1.write("\n" +"--------------------------" + "\n")
# read number of rows including header
with open(PyPoll) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    Total_Rows=sum(1 for line in csvfile)
    # Total_Rows - 1 = TotalVotes
    TotalVotes = (Total_Rows - 1)
    # print Total votes
    print(f"Total votes: {TotalVotes}")
    file1.write("\n" +f"Total votes: {TotalVotes}" + "\n")
    
print("-------------------------")
file1.write("\n" +"--------------------------" + "\n")

candidate_0_vote = 0
candidate_1_vote = 0
candidate_2_vote = 0
candidate_3_vote = 0

with open(PyPoll) as csvfile:
    csv_header = next(csvfile)
    for row in csvfile:
        #list of candidates who received votes
        row=row.strip()
        name = row.split(",")[2]
            
        if name not in candidate_names:
            candidate_names.append(name)
           # print(name[0] + )
            # To find the total number of votes each candidate
        if name == candidate_names[0]:
            candidate_0_vote += 1
        elif name == candidate_names[1]:
            candidate_1_vote += 1
        elif name == candidate_names[2]:
            candidate_2_vote += 1
        elif name == candidate_names[3]:
            candidate_3_vote += 1
            
    # calculate the percentage
    per_candidate0=str((candidate_0_vote/TotalVotes)*100)
    per_candidate1=str((candidate_1_vote/TotalVotes)*100)
    per_candidate2=str((candidate_2_vote/TotalVotes)*100)
    per_candidate3=str((candidate_3_vote/TotalVotes)*100)

    # display the candidate details(name, percentage of votes and number of votes)
    print(str(candidate_names[0]) + ": " + per_candidate0 + "% (" + str(candidate_0_vote) + ")")    
    print(str(candidate_names[1]) + ": " + per_candidate1 + "% (" + str(candidate_1_vote) + ")")    
    print(str(candidate_names[2]) + ": " + per_candidate2 + "% (" + str(candidate_2_vote) + ")")    
    print(str(candidate_names[3]) + ": " + per_candidate3 + "% (" + str(candidate_3_vote) + ")")
    # To display result in output file
    file1.write("\n" + str(candidate_names[0]) + ": " + per_candidate0 + "% (" + str(candidate_0_vote) + ")" +"\n" )
    file1.write("\n" + str(candidate_names[1]) + ": " + per_candidate1+ "% (" + str(candidate_1_vote) + ")" +"\n" )
    file1.write("\n" + str(candidate_names[2]) + ": " + per_candidate2 + "% (" + str(candidate_2_vote) + ")" +"\n" )
    file1.write("\n" + str(candidate_names[3]) + ": " + per_candidate3 + "% (" + str(candidate_3_vote) + ")" +"\n" )

    # announce the winner
    print("-------------------------")
    file1.write("\n" +"--------------------------" + "\n")
    if   (candidate_0_vote > candidate_1_vote) and (candidate_0_vote > candidate_2_vote) and (candidate_0_vote > candidate_3_vote):
        print("Winner: " + candidate_names[0])
        file1.write("\n" + "Winner: " + candidate_names[0] +"\n")
    elif (candidate_1_vote > candidate_2_vote) and (candidate_1_vote > candidate_3_vote):
        print("Winner: " + candidate_names[1])
        file1.write("\n" + "Winner: " + candidate_names[1] +"\n")
    elif (candidate_2_vote > candidate_3_vote):
        print("Winner: " + candidate_names[2])
        file1.write("\n" + "Winner: " + candidate_names[2] +"\n")
    else:
        print("Winner: " + candidate_names[3])
        file1.write("\n" + "Winner: " + candidate_names[3] +"\n")
    print("-------------------------")
    file1.write("\n" +"--------------------------" + "\n")
    file1.close()


 

