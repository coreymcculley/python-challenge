#import modules
import os
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
#load up database
bankcsvpath = os.path.join( 'Resources', 'budget_data.csv')
#initialize variable
dates=[]
profit=[]
profit_total=0
average_profit=0
dprofit=0
pro1=0
pro2=0
count=0
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
print(dmonth)
for i in range(0,length-1):
    profit_total+=int(profit[i])
    pro2=int(profit[i])
    if count > 0:
        dprofit+=pro2-pro1
        pro1=pro2
    print(dprofit)
    print(profit)
    count+=1

average_profit=round(dprofit/dmonth,2)
print(f"Total =$"+str(profit_total))
print(f"Avg =$"+str(dprofit))

