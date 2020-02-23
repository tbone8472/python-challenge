import os
import csv 

with open('Resources/election_data.csv', 'r') as csvfile:
	poll_reader = csv.reader(csvfile, delimiter=',')
	next(poll_reader)
	election_data = list(poll_reader)
 
         
for row in election_data:
    print(row)
#   print(row[0])
#   print(row[0],row[1],row[2],)