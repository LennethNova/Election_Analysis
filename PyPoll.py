#Assign a variable for the file to load and the path
#results = "Resources/election_results.csv"
import csv
import os
results = os.path.join("Resources","election_results.csv")

#Create a filename variable to a direct or indirect path to the file.
election_analysis = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file
with open(results) as election_data:
    #To do: perform analysis
    #print(election_data)
    # To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #Print each row in the csv file
    #for row in file_reader:
        #print(row)

    #Print header row
    headers = next(file_reader)
    print(headers)


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