import os
import csv

budgetPath = ("budget_data.csv")
months = []
pAndL = []
thisMonthRev = 0
lastMonthRev = 0
rev_change = 0
revChanges = []
with open(budgetPath, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        months.append(row[0])
        pAndL.append(row[1])
        thisMonthRev = int(row[1])
        rev_change = thisMonthRev - lastMonthRev
        revChanges.append(rev_change)
        lastMonthRev = thisMonthRev

pAndL = list(map(int,pAndL))
total = sum(pAndL)
total_formatted = "{0:,}".format(total)      
monthsCount = len(months)

total_rev_changes = sum(revChanges)
avg_rev_changes = total_rev_changes / monthsCount     
max_change = max(revChanges)
min_change = min(revChanges)
max_month_index = revChanges.index(max_change)
min_month_index = revChanges.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

print("The number of months in this period is " + str(monthsCount))
print("The total profit(loss) for this period is $" + str(total_formatted))
print("The average revenue change is $" + str(avg_rev_changes))
print("The greatest increase in revenue was " + max_month + " " + "$" + str(max_change))
print("The greatest decrease in revenue was " +  min_month + " " + "$" + str(min_change))

filepath =("output.txt")
with open(filepath,'w') as text:
    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write("The number of months in this period is " + str(monthsCount) + "\n") 
    text.write("The total profit(loss) for this period is $" + str(total_formatted) + "\n")
    text.write("The average revenue change is $" + str(avg_rev_changes) + "\n")
    text.write("The greatest increase in revenue was " + max_month + " " + "$" + str(max_change) + "\n")
    text.write("The greatest decrease in revenue was " +  min_month + " " + "$" + str(min_change) + "\n")