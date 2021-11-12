# Election Audit using Python 3.10

## Project Purpose and Overview
A Colorado Board of Elections employee requested an election audit to accurately tabulate election results. An election audit to determine which candidate won the election has already been provided to them, but they would now like to tabulate the county turnout.

The appropriate tasks to format and execute their request are as follows:
  
  1. Create a list of counties that received votes.
  2. Assign the correct vote count to each county.
  3. Determine the percentage of total votes each county received.
  4. Determine which county had the largest voter turnout.

After the calculations have been run, the data will be organized into a comprehensive format. The updated audit code will provide the Colorado Board of Elections with insight regarding county voter turnout.

## Resources
 - Data source: election_results.csv
 - Python 3.10.0 (used on Visual Studio Code)

## Election Audit Results
### The original election audit shows that:
  - There were 369,711 votes cast in the election.
  - The candidate results are:
    - Charles Casper Stockham received 23.0% of the total vote with 85,213 votes.
    - Diana Degette received 73.8% of the total vote with 272,892 votes.
    - Raymon Anthony Doane received 3.1% of the total vote with 11,606 votes.
  - The winner of the election was:
    - Dianace Degette who received 73.8% of the total vote with 272,892 votes.

      ![original_election_results](https://user-images.githubusercontent.com/92493572/141514869-972b4b35-3f5d-4629-88ae-64919ead7b7d.png)
[Figure 1]

The original code produced the results seen in Figure 1, but did not include county information.

### The updated election audit shows that:
  - All prior candidate data remains intact.
  - The county results are:
    - Arapahoe County accounted for 6.7% of the total vote with 24,801 votes.
    - Denver County accounted for 82.8% of the total vote with 306,055 votes.
    - Jefferson County accounted for the remaining 10.5% of the total vote with 38,855 votes.
  - The county that accounted for the largest portion of the vote count was:
    - Denver County with 82.8% contribution, totalling 306,055 votes.

      ![election_results](https://user-images.githubusercontent.com/92493572/141516533-8cb038af-2deb-46bc-83b8-383f1b0d5e30.png)
[Figure 2]

THe updated code produced the same results as Figure 1, but neatly added relevant county information.

## Election Audit Summary
