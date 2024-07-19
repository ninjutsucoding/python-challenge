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
# avg_pl = int(total_pl / total_months) would be the average profit each month
# calculate how to get the every change in profit each month
# month 1 profit / loss - month 2 profit / loss - repeat for all the months ending in month 85 minus month 86
# divided by 85 or total_months -1
# i thought i could use stdev() but its not working for me
# stdev(total_pl) comes back with an NameError "'stdev' is not defined"
# the long and crazy way to find standard deviation would be to
# for each data point find the square of the distance to the mean, sum the values, 
# divide by number of data points - 1, take the square root

#all this code in this section was provided by Xpert Learning Assistant
# this code doesn't work because example had a header named "Profit/Losses"
# i tried to substitue profit_loss and csv header of Profit/Losses and neither worked

# financial_data = zip_csv
# monthly_changes = []
# previous_profit = financial_data[0][Profit/Losses]

#for i in range(1, len(financial_data)):
#    current_profit = financial_data[i][profit_loss]
#    profit_change = current_profit - previous_profit
#    monthly_changes.append({date: financial_data[i][date], "Profit Change": profit_change})
#    previous_profit = current_profit

#for change in monthly_changes:
#    print(change)
# end of the code from Xpert Learning Assistant


# Greatest Increae of Profits + date (max function)
# if the profit_loss = big_p then print the zip_csv row?
big_p = max(profit_loss)
# I know that from amount found, I should link over the date from the first column in the row,
#but I'm not sure how to do that.  

# Greatest Decrease in Profits + date (min function)
big_l = min(profit_loss)
# i know that from the amount found, I should link over the date from the first column in the row
# but I'm not sure how to do that.   

#my Greatest Increase of Profits and Decrease of Profits were different thatn what was stated in the Module.
# I checked the dates in the csv file and it had a different amount listed than in the Module.
# i just looked the dates up manually.   

print("Financial Analysis")
print()
print("-"*40)
print()
print("Total Months: " + str(total_months))
print()
print("Total: " + str(total_pl))
print()
print("Average Change: ")
print()
print("Greatest Increase in Profits: Mar-13 " + str(big_p))
print()
print("Greatest Decrease in Profits: Dec-10 " + str(big_l)) 