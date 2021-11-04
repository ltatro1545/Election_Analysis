import csv
import os
#assigns variable for the file to load from a path and a variable to save to a path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print header row.
    headers = next(file_reader)
    print(headers)

# close the file
election_data.close()












# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    
    # Write some data to the file.
    txt_file.write("Counties in the Election\n------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")


# Close the file
txt_file.close()