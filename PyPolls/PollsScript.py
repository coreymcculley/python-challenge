#import modules
import os
import csv
import numpy as np

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
per_c1=round(100*c1/c_total,3)
per_c2=round(100*c2/c_total,3)
per_c3=round(100*c3/c_total,3)
per_c4=round(100*c4/c_total,3)

print(c_total)
print(per_c1)
print(per_c2)
print(per_c3)
print(per_c4)
