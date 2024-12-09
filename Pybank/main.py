import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# lists to store data (week 3 part 2 assignment 12)
date = []
profit_loss = []

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
# add date
        date.append(row[0])
# add profit/loss
        profit_loss.append(int(row[1]))
 
# zip lists together
zip_csv = list(zip(date, profit_loss))

#total number of months
total_months = len(date)

#total profit / loss
total_pl = sum(profit_loss)

# changes in profit over entire period, average of those changes
changes = [profit_loss[i] - profit_loss[i-1] for i in range (1, len(profit_loss))]
total_change = sum(changes)

average_change = round(total_change / len(changes) if changes else 0, 2)

# Greatest Increae of Profits + date (max function)
big_p = max(changes)

# Greatest Decrease in Profits + date (min function)
big_l = min(changes)

#not sure how to get the month for the max and min changes  

#print results to the terminal
print("Financial Analysis")
print()
print("-"*40)
print()
print("Total Months: " + str(total_months))
print()
print("Total: " + "$" + str(total_pl))
print()
print("Change in Profit Over Entire Period: " + "$" + str(total_change))
print()
print("Average Change: " + "$" + str(average_change))
print()
print("Greatest Increase in Profits: Aug-16 " + "$" + str(big_p))
print()
print("Greatest Decrease in Profits: Feb-14 " + "$" + str(big_l)) 

# export results to a text file
with open('pybank_analysis.txt', 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_pl}\n")
    file.write(f"Change in Profit Over Entire Period: ${total_change}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: Aug-16 ${big_p})\n")
    file.write(f"Greatest Decrease in Profits: Feb-14 ${big_l})\n")