import csv
import os
import sys

intro = "Election Results\n---------------------"

# Open file
with open(os.path.join (sys.path[0],"Resources\\election_data.csv"),'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    header = next(csv_reader)
    list_of_rows = list(csv_reader)

    row_number = 0
    prev_candidate = ""
    candidates = []
    final_results = []
    

    if header != None:
        for rows in list_of_rows:
            row_number += 1
            candidates.append(rows[2])
                   
    sorted_candidates = list(set(candidates)) 

    dd_candid = sorted_candidates[0]  
    ccs_candid = sorted_candidates[1] 
    rad_candid = sorted_candidates[2] 

    dd_votes = candidates.count(dd_candid)
    ccs_votes = candidates.count(ccs_candid)
    rad_votes = candidates.count(rad_candid)

    dd_percent = round(dd_votes / row_number * 100, 3)
    ccs_percent = round(ccs_votes / row_number * 100, 3)
    rad_percent = round(rad_votes / row_number * 100, 3)

    final_results.append((dd_candid, dd_votes, dd_percent))
    final_results.append((ccs_candid, ccs_votes, ccs_percent))
    final_results.append((rad_candid, rad_votes, rad_percent))

    winner_amount = max(dd_votes, ccs_votes, rad_votes)
    winner = ""

    for x in (0,2):
        if winner_amount == final_results[x][1]:
            winner = final_results[x][0]
    
    print(intro)
    print(f'Total Votes: {row_number}')
    print('---------------------')
    print(f'{ccs_candid}: {ccs_percent}% ({ccs_votes})')
    print(f'{dd_candid}: {dd_percent}% ({dd_votes})')
    print(f'{rad_candid}: {rad_percent}% ({rad_votes})')
    print('---------------------')
    print(f'Winner: {winner}')
    print('---------------------')

    with open(os.path.join (sys.path[0],"Analysis\\Election Data Output.txt"),'w') as f: 
        f.write(f'{intro}\nTotal Votes: {row_number}\n---------------------\n{ccs_candid}: {ccs_percent}% ({ccs_votes})\n{dd_candid}: {dd_percent}% ({dd_votes})\n{rad_candid}: {rad_percent}% ({rad_votes})\n---------------------\nWinner: {winner}\n---------------------')

    