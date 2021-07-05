# Election_Challenge

## Election Audit Overview
A Colorado Board of Elections employee has requested an election audit of a recent local congressional election with the following outputs:

1. Total number of votes cast
2. A complete list of candidates who received votes
3. Total number of votes each candidate received
4. Percentage of votes each candidate won
5. The winner of the election based on popular vote
6. Breakdown of the number of votes and the percentage of total votes for each county in the precinct
7. Which county had the largest number of votes?


## Resources
-Data Source: election_results.csv 
(location: https://github.com/Roland791/election_analysis/blob/main/Resources/election_results.csv)
- Python Script: PyPoll_Challenge.py
(location: https://github.com/Roland791/election_analysis/blob/main/PyPoll_Challenge.py)
-Software: Python 3.9, Visual Studio Code 1.57.1

## Election Audit Results
The analysis of the election shows that:

1. There were 369,711 votes cast in the election. 
2. The candidates were 
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
3. The total number of votes each candidate received were
	- Charles Casper Stockham: 85,213
	- Diana DeGette: 272,892
	- Raymon Anthony Doane: 11,606
4. The total percentage of votes each candidate received were
	- Charles Casper Stockham: 23.0%
	- Diana DeGette: 73.8%
	- Raymon Anthony Doane: 3.1%
5. The winner of the election was:
	- Winner: Diana DeGette
	- Winning Vote Count: 272,892
	- Winning Percentage: 73.8%
6. The County Votes were
	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
7. The county with the most votes was
	- Denver (306,055)

## Election Audit Results File
- Results File: election_results.txt
(location: https://github.com/Roland791/election_analysis/blob/main/analysis/election_results.txt)
	
##Election Audit Summary

This election audit analysis was able to automate the counting of vote data based on multiple criteria including counts per candidate and per county. 
With additional columns of data, the results could be expanded for other elections or to provide deeper analysis, such as: 
	1) Expanding to federal elections by including state data and looping through the same code with different variables (modifying "county" variables to read "state" and pointing to a state based column)
	2) Adding political affiliation of the candidates and creating if statements to determine the political leanings of each county based on the percentage of the population that voted for each candidate