import csv
import os
months_data = []
mylistdata = []
pnl_list_data = []
avgchg_data = []
total_pnl = 0
avgchg_total = 0
gt_inc = 0
gt_dec = 0
gt_inc_mnth = ""
gt_dec_mnth = ""

#open csv
with open('Resources/budget_data.csv', 'r') as csvfile:
  filereader = csv.reader(csvfile, delimiter=',')
  next(filereader)
  mylistdata = list(filereader)

#print(mylistdata)
  i = 1
  for row in mylistdata:
    months_data.append(row[0])
    pnl_list_data.append(int(row[1]))
      
# get pnl total and count of months
total_pnl = sum(pnl_list_data)    
total_mths = len(mylistdata)
#find average changes
i= 0
n = 0
for i in range(len(pnl_list_data)-1):
    n = i + 1
    avgchg_data.append((pnl_list_data[n]) - (pnl_list_data[i]))
avgchg_total = format(sum(avgchg_data) / (total_mths -1), ".2f")
gt_inc = max(avgchg_data)
gt_dec = min(avgchg_data)
# find the month for greatest increase
for i in range(len(avgchg_data)):
    if avgchg_data[i] == gt_inc:
      gt_inc_mnth = months_data[i + 1]
# find the month for greatest decrease
for i in range(len(avgchg_data)):
    if avgchg_data[i] == gt_dec:
      gt_dec_mnth = months_data[i + 1]
print("Financial Analysis")
print("-" * 35)
print(f"Total Months: {total_mths}")
print(f"Total: ${total_pnl}")
print(f"Average Change: ${avgchg_total}")
print(f"Greatest Increase in Profits: {gt_inc_mnth} (${gt_inc})")
print(f"Greatest Decrease in Profits: {gt_dec_mnth} (${gt_dec})")
# write resulst to text file.
file = open("report.txt", "w")
file.write("Financial Analysis\n")
file.write("-" * 35)
file.write(f"\nTotal Months: {total_mths}\n")
file.write(f"Total: ${total_pnl}\n")
file.write(f"Average Change: ${avgchg_total}\n")
file.write(f"Greatest Increase in Profits: {gt_inc_mnth} (${gt_inc})\n")
file.write(f"Greatest Decrease in Profits: {gt_dec_mnth} (${gt_dec})\n")
# make sure the file is closed
file.close()