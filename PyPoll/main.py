import csv

# Provide the path to election_data.csv file
input_csv_file_path = "C:/Users/ipsit/Documents/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv"

def analyze_election_data(input_csv_file_path, output_file_path):
    # Initialize variables
    total_votes = 0
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0

    # Read the CSV file
    csv_file = open(input_csv_file_path)
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row

    # Loop through rows in the CSV file
    for row in csv_reader:
        # Process each row
        total_votes += 1
        candidate = row[2]

        # Count votes for each candidate
        if candidate == "Charles Casper Stockham":
            charles_votes += 1
        elif candidate == "Diana DeGette":
            diana_votes += 1
        elif candidate == "Raymon Anthony Doane":
            raymon_votes += 1

    # Calculate the percentage of votes each candidate won
    percentage_1 = (charles_votes / total_votes) * 100
    percentage_2 = (diana_votes / total_votes) * 100
    percentage_3 = (raymon_votes / total_votes) * 100

    # Determine the winner
    if charles_votes > diana_votes and charles_votes > raymon_votes:
        winner = "Charles Casper Stockham"
    elif diana_votes > charles_votes and diana_votes > raymon_votes:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"

    # Prepare the results string
    results = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
        f"Candidate 1: {percentage_1:.3f}% ({charles_votes})\n"
        f"Candidate 2: {percentage_2:.3f}% ({diana_votes})\n"
        f"Candidate 3: {percentage_3:.3f}% ({raymon_votes})\n"
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )

    # Print the results to the terminal
    print(results)

    # Write the results to a text file
    with open(output_file_path, "w") as output_file:
        output_file.write(results)


# Provide the path for the output text file
output_file_path = "C:/Users/ipsit/Documents/GitHub/Python-Challenge/PyPoll/Analysis/election_results.txt"

# Call the function with the file paths
analyze_election_data(input_csv_file_path, output_file_path)
