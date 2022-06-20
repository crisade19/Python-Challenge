import csv
import os
import sys

intro = "Financial Analysis\n---------------------"
total = 0

# Import file
with open(os.path.join (sys.path[0],"Resources\\budget_data.csv"),'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    header = next(csv_reader)
    list_of_rows = list(csv_reader)
    row_number = 0
    prev_profit = 0
    profits = []
    max_value = 0
    min_value = 0
    row = 0
    total_diff = 0

    if header != None:
        for rows in list_of_rows:
            row_number += 1

            profit = int(rows[1])
            total = total + profit
            if prev_profit == 0:
                diff = 0
                profits.append((rows, diff))
                prev_profit = profit
                continue
            else:
                if profit < 0:
                    diff = -(prev_profit - profit)
                    profits.append((rows, diff))
                elif profit > 0 and profit > prev_profit:
                    diff = profit - prev_profit
                    profits.append((rows, diff))
                elif profit > 0 and profit < prev_profit:
                    diff = -(prev_profit - profit)
                    profits.append((rows, diff))
                elif prev_profit < 0:
                    diff = (profit - prev_profit)
                    profits.append((rows, diff))
                elif prev_profit > 0 and prev_profit > profit:
                    diff = -(prev_profit - profit)
                    profits.append((rows, diff))
                elif prev_profit >0 and prev_profit < profit:
                    diff = profit - prev_profit
                    profits.append((rows, diff))
            prev_profit = profit
    
    for records in profits:
        if max_value == 0 or profits[row][1] > max_value:
            max_value = profits[row][1]
            max_month = profits[row][0][0]

        if min_value == 0 or profits[row][1] < min_value:
            min_value = profits[row][1]
            min_month = profits[row][0][0]
        total_diff = total_diff + profits[row][1]
        row += 1
    average_diff = round(total_diff / (row-1), 2)

    print (f'{intro}')
    print (f'Total Months: {row_number}')
    print (f'Total: ${total}')
    print (f'Average Change: ${average_diff}')
    print (f'Greatest Increase in Profits: {max_month} (${max_value})')
    print (f'Greatest Decrease in Profits: {min_month} (${min_value})')


with open(os.path.join (sys.path[0],"Analysis\\Budget Data Output.txt"),'w') as f:
    f.write(f'{intro}\nTotal Months: {row_number}\nTotal: ${total}\nAverage Change: ${average_diff}\nGreatest Increase in Profits: {max_month} (${max_value})\nGreatest Decrease in Profits: {min_month} (${min_value})')
