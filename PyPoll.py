import csv
import os
# Assigns variable for the file to load from a path and a variable to save to a path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:

        total_votes += 1

        # Acquire candidate name for each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


# Save results to a txt file
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes to PyPoll and election_analysis.txt
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)


    # # Print the candidate list
    # print(candidate_options)
    # print(candidate_votes)
    # print(f"{total_votes:,}")




# close the file
election_data.close()


# Close the file
txt_file.close()