import os
import csv
import pandas as pd
from collections import OrderedDict

total_votes = 0
# candidate_lst = []
# candidate_pct = []
# total_votes_won = []
# winner_elect = []

with open('Resources/election_data.csv', 'r') as csvfile:
	pollreader = csv.reader(csvfile, delimiter=',')
	next(pollreader)
	
	for row in pollreader:
		total_votes += 1
 	
    	if row[2] == "Khan": 
     	votes_khan += 1	
      
    	elif row[2] == "Correy":
      	votes_correy += 1
    
    	elif row[2] == "Li":
      	votes_li += 1
      
    	elif row[2] == "O'Tooley":
      	votes_otooley += 1
         
candidate_totals = [votes_correy, votes_otooley, votes_khan, votes_li]
print(candidate_totals)
    


# Report
# print("Financial Analysis")
# print("----------------------------")
#print(f"Total Months:{total_mths}")

#print(f"Total Profits and Losses:${total_pnl}")
#print(f"Average Change Per month:{avgchg_mth}") 