#import modules
import os
import csv
#load up database
pollcsvpath = os.path.join( 'Resources', 'election_data.csv')
#initialize variables
voter_id=[]
county=[]
candidate=[]
c1=0
c2=0
c3=0
c4=0
c_total=0
winner=""
#open database
with open(pollcsvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data = [word for word in [row for row in csvreader]]
length=len(data)
#extract columns into single lists
for i in range(1,length):
    voter_id.append(data[i][0])
    county.append(data[i][1])
    candidate.append(data[i][2])
length=len(candidate)
#Add total vote counts and votes for each candidate
for i in range(0,length):
    c_total+=1
    if candidate[i] == "Khan":
        c1+=1
    if candidate[i] == "Correy":
        c2+=1
    if candidate[i] == "Li":
        c3+=1
    if candidate[i] == "O'Tooley":
        c4+=1
#Calculate percentages for each candidate
per_c1=round(100*c1/c_total,3)
per_c2=round(100*c2/c_total,3)
per_c3=round(100*c3/c_total,3)
per_c4=round(100*c4/c_total,3)
percents=[per_c1,per_c2,per_c3,per_c4]
#Determine winner
if per_c1 == max(percents):
    winner="Khan"
if per_c2 == max(percents):
    winner="Correy"
if per_c3 == max(percents):
    winner="Li"
if per_c4 == max(percents):
    winner="O'Tooley"
#Print out results and create Txt file
results = f"""Election Results
------------------------------------
Total Votes: {c_total}
------------------------------------
Khan: {per_c1}% ({c1})
Correy: {per_c2}% ({c2})
Li: {per_c3}% ({c3})
O'Tooley: {per_c4}% ({c4})
------------------------------------
Winner: {winner}"""
print (results)
export_results = ''.join(results)
txtpath = os.path.join ( "Resources", "PyPoll_Summary_Results.txt")
with open (txtpath,'w') as file: 
   file.write(export_results)