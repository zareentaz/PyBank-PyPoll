import os
import csv
 # path for the file
pybank = "budget_data.csv"
totalmonths=[]
total= []
average_change=[]

# Reading using csv module
with open(pybank, newline="", encoding="utf-8")as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvwriter = csv.writer(csvfile,delimiter=',')
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    for row in csvreader:
        totalmonths.append(row[0])
        #total+=int(row[1])
        total.append(int(row[1]))
#average of changes
    for i in range(len(total)-1):
        average_change.append(total[i+1]-total[i])

# Greatest increase  and decrease in profit
Greatest_profit=max(average_change)
Greatest_loss=min(average_change)

#Max and min of months
Max_month=average_change.index(max(average_change))+1
Min_month=average_change.index(min(average_change))+1

print("Financial Analysis")
 
# print the result in terminal and output.txt file
print("-------------------------------------------------------")
print("Total Months: " +str(len(totalmonths)))
print(f"Total: ${sum(total)}")
print(f"Average Change: ${round(sum(average_change)/len(average_change),2)}")
print(f"Greatest Increase in Profits:{totalmonths[Max_month]} (${Greatest_profit})")
print(f"Greatest Decrease in Profits:{totalmonths[Min_month]} (${Greatest_loss})")
file1=open("output.txt","w")
file1.write("Financial Analysis \n -----------------------------------------------  ")
file1.write("\n" +"Total Months: " +str(len(totalmonths))+ "\n")
file1.write("\n" + f"Total: ${sum(total)}" +"\n")
file1.write("\n" + f"Average Change: ${round(sum(average_change)/len(average_change),2)}" + "\n" )
file1.write("\n" + f"Greatest Increase in Profits:{totalmonths[Max_month]} (${Greatest_profit})" + "\n" )
file1.write("\n" + f"Greatest Decrease in Profits:{totalmonths[Min_month]} (${Greatest_loss})" + "\n" )
file1.close()
