import os
import csv

totalnum_votes = [0]
# candidate_lst = []
# candidate_pct = []
# total_votes_won = []
# winner_elect = []



with open('Resources/election_data.csv', 'r') as csvfile:
	poll_reader = csv.reader(csvfile, delimiter=',')
	next(poll_reader)
	election_data = list(poll_reader)
 
 # total number of votes
# totalnum_votes = len(poll_reader([2])
         
for row in election_data:
    print(row)
#   print(row[0])
#   print(row[0],row[1],row[2],)





# Report
# print("Financial Analysis")
# print("----------------------------")
#print(f"Total Months:{total_mths}")

#print(f"Total Profits and Losses:${total_pnl}")
#print(f"Average Change Per month:{avgchg_mth}") 
	











