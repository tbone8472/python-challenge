import csv
pnl_list = []
total_pnl = [0]

with open('Resources/budget_data.csv', 'r') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',')
	next(filereader)
	mylistdata = list(filereader)
for row in mylistdata:
    

# total number of months for entire data set
    total_mths = len(mylistdata)
print(total_mths)

# Net Profit and Loss
i = 0
for row in mylistdata:
	pnl_list.append(row[1])
	pnl_list = [int(i) for i in (pnl_list)
    total_pnl = (sum)(pnl_list)
# print(total_pnl)
  


