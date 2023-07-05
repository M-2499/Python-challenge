'PyBank'

import os
import csv

# Set the path for the input file
file_path = "C:/Users/Andrews/OneDrive/UTDataBootcamp/Python-challenge/PyBank/Resources/budget_data.csv"


# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ""
greatest_decrease_month = ""

# Read the CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    header = next(csv_reader)
    
    # Loop through the rows in the CSV file
    for row in csv_reader:
        # Increment the total number of months
        total_months += 1
        
        # Calculate the net total
        net_total += int(row[1])
        
        # Calculate the change in profit/loss from the previous month
        change = int(row[1]) - previous_profit_loss
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = int(row[1])
        
        # Calculate the total change
        total_change += change
        
        # Check if the current change is the greatest increase or decrease
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]
        
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]

# Calculate the average change
average_change = round(total_change / (total_months - 1), 2)

# write the text file containing results
file_path= "C:/Users/Andrews/OneDrive/UTDataBootcamp/Python-challenge/PyBank/Analysis/results.txt"
with open(file_path, 'w') as file:



    
# Print the financial analysis
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

