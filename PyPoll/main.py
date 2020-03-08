import os 
import csv

# total votes for election
total_votes = 0
# container for votes per candidate
votes_correy = 0
votes_khan = 0
votes_li = 0
votes_otooley = 0
# percentage of total vote per candidate
pct_correy = 0.000
pct_khan = 0.000
pct_li = 0.000
pct_otooley = 0.000
#reading the csv
with open ('Resources/election_data.csv','r') as csvfile:
    pollreader = csv.reader(csvfile,delimiter=',')
    next(pollreader)
    for row in pollreader:
        total_votes += 1
        if row[2] == "Correy":
            votes_correy += 1
        elif row[2] == "Khan":
            votes_khan += 1
        elif row[2] == "Li":
            votes_li += 1
        elif row[2] == "O'Tooley":           
            votes_otooley += 1
          
candidate_totals = [votes_correy, votes_khan, votes_li, votes_otooley]
#sort the list
sorted_list = sorted(candidate_totals, reverse=True)
# vote percentage per candidate
pct_correy = format((((votes_correy/total_votes) * 100)),'.3f')
pct_khan = format((((votes_khan/total_votes) * 100)),'.3f')
pct_li = format((((votes_li/total_votes) * 100)),'.3f')
pct_otooley = format((((votes_otooley/total_votes) * 100)),'.3f')
  
file = open("results.txt", "w")
print()
print("Election Results")
file.write(f"Election Results\n")
print("--" * 30)
file.write("-" * 30)
print(f"Total Votes: {total_votes}")
file.write(f"\nTotal Votes: {total_votes}\n")
print("--" * 30)
print()
file.write("-" * 30)
for s in sorted_list:
      if s == votes_correy:
          print(f"Correy:  {pct_correy}% ({votes_correy})")
          print()
          file.write(f"\nCorrey:  {pct_correy}% ({votes_correy})\n")
      elif s == votes_otooley:
        print(f"O'Tooley: {pct_otooley}% ({votes_otooley})")
        print()
        file.write(f"\nO'Tooley: {pct_otooley}% ({votes_otooley})\n")
      elif s == votes_khan:
        print(f"Khan: {pct_khan}% ({votes_khan})")
        print()
        file.write(f"\nKhan: {pct_khan}% ({votes_khan})\n")
      elif s == votes_li:
        print(f"Li: {pct_li}% ({votes_li})")
        print()
        file.write(f"\nLi: {pct_li}% ({votes_li})\n")
        file.write("-" * 30 )
        if votes_correy == sorted_list[0]:
            overall_winner = "Correy"
        elif votes_otooley == sorted_list[0]:
            overall_winner = "O'Tooley"
        elif votes_khan == sorted_list[0]:
            overall_winner = "Khan"
        elif votes_li == sorted_list[0]:
            overall_winner = "Li"
    
print("-" * 30 )
print(f"\nWinner: {overall_winner}\n")
file.write(f"\nWinner: {overall_winner}\n")
print("-" * 30 )
file.write("-" * 30 )
# make sure to close the file we are writing the Election Results to
file.close()
           
  
  
  
  
                 
