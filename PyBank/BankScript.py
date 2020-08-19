#import modules
import os
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
#load up database
bankcsvpath = os.path.join( 'Resources', 'budget_data.csv')
#initialize variables
dates=[]
profit=[]
average_profit=0
dprofit=[]
pro2=0
count=0
max_pro=0
min_pro=0
#open database
with open(bankcsvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    data = [word for word in [row for row in csvreader]]
    length=len(data)
    #extract profit and dates into single list
    for i in range(1,length):
        dates.append(data[i][0])
        profit.append(data[i][1])


#calculate the number of months from first to last entry
d1=datetime.strptime(dates[0],'%b-%Y')
d2=datetime.strptime(dates[len(dates)-1],'%b-%Y')
dt=relativedelta(d2,d1)
dmonth=dt.months+dt.years*12+1

#Calculate Profit total and average change
pro1=int(profit[0])
profit_total=int(profit[0])
for i in range(1,length-1):
    profit_total+=int(profit[i])
    pro2=int(profit[i])
    if count > 0:
        dprofit.append(pro2-pro1)
        pro1=pro2    
    count+=1
average_profit=round(sum(dprofit)/(len(dprofit)+1),2)

#Find max and min months and profit (+2 for losing a row for each the header and the delta profit)
for i in range(1,len(dprofit)-1):
    max_pro=max(dprofit)
    if dprofit[i] == max_pro:
        count=i+2
max_mon=dates[count]
for i in range(1,len(dprofit)):
    min_pro=min(dprofit)
    if dprofit[i] == min_pro:
        count=i+2
min_mon=dates[count]

#Print out results and create Txt file
results = f"""Financial Analysis
------------------------------------
Total Months: {dmonth}
Total: $ {profit_total}
Average Change: $ {average_profit}
Greatest Increase in Profits: {max_mon} ($ {max_pro})
Greatest Decrease in Profits: {min_mon} ($ {min_pro})"""
print (results)
export_results = ''.join(results)
txtpath = os.path.join ( "Resources", "PyBank_Summary_Results.txt")
with open (txtpath,'w') as file: 
   file.write(export_results) 