import os 
import csv

pnl_list_data = []
total_mths = []
total_pnl = []



with open('Resources/budget_data.csv', 'r') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',')
	next(filereader)
	mylistdata = list(filereader)

i = 0
for row in mylistdata[1]:
	pnl_list_data.append(row[1])
pnl_list_data = [int(i) for i in pnl_list_data] 
total_pnl = (sum)(pnl_list_data)
print(pnl_list_data)

total_mths = len(mylistdata)
print(total_mths)


for row in pnl_list_data:
	variance_mth = (pnl_list_data[i]) - (pnl_list_data[i - 1])/total_pnl
print(variance_mth)
print(pnl_list_data[i])