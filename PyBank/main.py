import csv

# Provide the path to the input budget_data.csv file
csv_file_path = "C:/Users/ipsit/Documents/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv"

def budget_data(input_csv_file_path, output_file_path):
    # Initialize variables for total number of months, profit and loss, greatest increase and decrease dates and amounts
    total_months = 0
    final_profit_loss = 0
    previous_profit_loss = 0
    monthly_changes = []
    greatest_increase_date = ""
    greatest_increase_amount = float("-inf")
    greatest_decrease_date = ""
    greatest_decrease_amount = float("inf")

    # Read the CSV file
    csv_file = open(input_csv_file_path)
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)  

    # Loop through each row in the CSV file
    for row in csv_reader:
        # Process each row 
        date = row[0]
        running_profit_loss = int(row[1])

        # Calculate total number of months and net total prfit and loss
        total_months += 1
        final_profit_loss += running_profit_loss

        # Calculate monthly change
        if total_months > 1:
            change = running_profit_loss - previous_profit_loss
            monthly_changes.append(change)

            # Update greatest increase and decrease
            if change > greatest_increase_amount:
                greatest_increase_date = date
                greatest_increase_amount = change
            elif change < greatest_decrease_amount:
                greatest_decrease_date = date
                greatest_decrease_amount = change

            # Update previous profit/loss for the next iteration
            previous_profit_loss = running_profit_loss

    # Calculate average change
    if total_months > 1:
        average_change = sum(monthly_changes) / (total_months - 1) 
    else:
        average_change = 0


    # Prepare the results string
    results = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Net Total: ${final_profit_loss}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})"
    )

    # Print the results
    print(results)

    # Write the results to a text file
    with open(output_file_path, "w") as output_file:
        output_file.write(results)


# Provide the path for the output text file
output_file_path = "C:/Users/ipsit/Documents/GitHub/Python-Challenge/PyBank/Analysis/budget_data_results.txt"

# Call the function with the file paths
budget_data(csv_file_path, output_file_path)
