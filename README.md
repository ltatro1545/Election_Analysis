# Election Audit Enhancement Using Python 3.10

## Project Purpose and Overview
A Colorado Board of Elections employee requested an election audit to accurately tabulate election results. An election audit to determine which candidate won the election has already been provided to them, but they would now like to tabulate the county turnout.

The appropriate tasks to format and execute their request is as follows:
  
  1. Create a list of counties that received votes.
  2. Assign the correct vote count to each county.
  3. Determine the percentage of total votes each county received.
  4. Determine which county had the largest voter turnout.

After the calculations have been run, the data will be organized into a comprehensive format. The updated audit code will provide the Colorado Board of Elections with insight regarding raw county voter turnout.

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

The original code produced the results seen in Figure 1. Note that it did not include county information.

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

The updated code produced the same results as Figure 1, but neatly added relevant county information.

## Election Audit Summary
The script produced during this project adequately incorporates county data into the results, and even has the potential to do much more. First, it is important to note that the voter turnout was calculated based off of total votes received - it did not incorporate county population, which is important to note when comparing the percentage of voter turnout. For instance, the 2020 census report shows the following populations of each county:
  - Arapahoe County: 655,070
  - Denver County: 705,576
  - Jefferson County: 582,881

Though it may be important to calculate which county contributed the highest number of raw votes, there could also be a calculation to determine which county had the highest participation rate. This would be done by simply dividing the county vote by its population.

![county_turnout_code](https://user-images.githubusercontent.com/92493572/141523837-315dea8e-335e-4d33-8a82-75ce9d82c26d.png)
![county_turnout_output](https://user-images.githubusercontent.com/92493572/141523839-8095f3b6-1f61-41ba-b93e-88852964f05b.png)

[Figure 3] & [Figure 4] 

As seen above, a dictionary was created to hold county populations, followed by a script to pull the values from that dictionary and assign it a variable "countypop". The voter participation was then calculated in the same as "vote_percentage" (above), but used the new "countypop" variable in place of "total_votes". At the bottom of Figure 3, an extra line was added to "county_results" to include voter participation. This was done in a neat and tidy way to compliment the original results. The output of that script is seen in Figure 4.

Finally, it may be worthwhile to look at individual subdivisions of each county (sometimes called "beats" or "zones"), and determine their voter participation. First, this column of information would need to be included in the csv file. After that, one would make a Python list to hold all of the subdivisions, a dictionary to hold each subdivision's vote count, and then assign a variable to the subdivision column. This process would look nearly identical to tabulating county votes.
