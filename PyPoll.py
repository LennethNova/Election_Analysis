#Assign a variable for the file to load and the path
#results = "Resources/election_results.csv"
# Dependencies
import csv
import os
file_to_load = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Assign a variable a total vote counter
total_votes = 0

#List of candidates
candidate_options = []

# Dictionary
candidate_votes = {}

#Winning count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:
    #To do: perform analysis
    #print(election_data)
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Print header row, if I use the print.
    #Without print it will skip the first row
    headers = next(file_reader)
    #print(headers)

    #Print each row in the csv file
    for row in file_reader:
        #print(row)

        total_votes += 1
#Print total votes
#print(f"{total_votes: ,}")

    #Print candidate name
        candidate_name = row[2]

        #If the candidate does not maych any existing candidate
        if candidate_name not in candidate_options:
            #Add it to the list of candidates

        #Add my candidate name options to the candidate name list
            candidate_options.append(candidate_name)

            #Begin tracking the votes for the candidates
            candidate_votes[candidate_name] = 0

        #Add the vote to that candidate
        candidate_votes[candidate_name] += 1

#Save results to that candidate's count
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"------------------------\n"
    )
    #Save the final vote count to the text file
    print(election_results, end="")
    txt_file.write(election_results)

    #Determine the percentage votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes) * 100

        #Results
        candidate_results = (f"{candidate_name}: {vote_percentage: .1f}% ({votes: ,})\n")

        #Print each candidate
        print(candidate_results)
        txt_file.write(candidate_results)

        #Print results, if this is outside the for loop it will only print the last one
        #print(f"{candidate_name}: received {vote_percentage: .1f}% of the vote.")
        
        #Determine the winning count and candidate
        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set the winnning count = winning percent = vote percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning candidate name
            winning_candidate = candidate_name


        #Print results, if this is outside the for loop it will only print the last one
        #print(f"{candidate_name}: {vote_percentage: .1f}% ({votes: ,})\n")

    winning_candidate_summary = (
        f"------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"------------------------\n")


    #Candidate summary
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)




    


#Using the with statement open the file as a text file
#with open(election_analysis,"w") as txt_file:
    # Write some data to the file
    #txt_file.write("Hello World!")
 #   txt_file.write("Counties in the election\n------------------------\n")
# Write 3 counties to the file
    #txt_file.write("Arapahoe, ")
    #txt_file.write("Denver, ")
    #txt_file.write("Jefferson, ")
    #txt_file.write("Arapahoe, Denver, Jefferson")
   # txt_file.write("Arapahoe\nDenver\nJefferson")

#Using the with statement open the file as a text file
#outfile = open(election_analysis, "w")

#write some data to the file
#outfile.write("Hello World!")

#Close the file
#outfile.close()

#Open the election results and read the file
#election_data = open(results, "r")

# Using the open() function with teh "w" mode we will write data to the file
#open(election_analysis, "w")

#to do: perform analysis

#close the file, its important that you always close a file that you opened
#election_data.close()