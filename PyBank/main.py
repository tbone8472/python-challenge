import csv

variance = []

total_pnl = [0]

_mth = []

avgchg_total = []

avgchg_data = []

gt_inc = []

gt_dec = [] 

pnl_list_data = []

with open('Resources/budget_data.csv', 'r') as csvfile:
	filereader = csv.reader(csvfile, delimiter=',')
	next(filereader)
	mylistdata = list(filereader)

i = 1
for row in mylistdata:
	pnl_list_data.append(row[1])
pnl_list_data = [int(i) for i in pnl_list_data] 
total_pnl = (sum)(pnl_list_data)
print(pnl_list_data) 
			
total_mths = len(mylistdata)

i = 1
for i in range(len(pnl_list_data)):
	avgchg_mth = (pnl_list_data[i]) - (pnl_list_data[i - 1])
print({avgchg_mth})
     
   

    
# Report
# print("Financial Analysis")
# print("----------------------------")
print(f"Total Months:{total_mths}")

print(f"Total Profits and Losses:${total_pnl}")
print(f"Average Change Per month") 
	
         