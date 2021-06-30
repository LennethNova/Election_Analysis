print("Hello World")

type(3)

counties = ["Arapahoe","Denver","Jefferson"]
print(counties)

counties[1] = "El Paso"
print(counties)
counties.remove("Arapahoe")
print(counties)
counties.append("Denver")
print(counties)
counties.append("Arapahoe")
print(counties)

#to make a dictionary
counties_dict = {}
#If I want to add a value to my dictionary in the git bash
counties_dict["Arapahoe"] = 422829
#this adds the 3 elements to my dictionary
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#list for my dictionaries
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(voting_data)

voting_data.insert(1, {"county": "El Paso", "registered_voters": 461149})
print(voting_data)
#voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
#print(voting_data)
voting_data.pop(0)
print(voting_data)
voting_data.append({"county":"Denver", "registered_voters": 463353})
print(voting_data)
voting_data.pop(1)
print(voting_data)
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#1. percentage_votes = (my_votes / total_votes) * 100
#2. print("I received " + str(percentage_votes)+"% of the total votes.")
#print("I received " + str(round(percentage_votes,2))+"% of the total votes.")
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
    #print(counties[1])

if counties[2] != "Jefferson":
    print(counties[2])

    #------------
for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for i in counties_dict:
    print(counties_dict.get(i))

#for key,value in counties_dict.items():
for county, voters in counties_dict.items():
    #print(key, value)
    print(county, voters)

#----- They give me the info in string
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f" {county} county has {voters:,} registered voters.")

#--------
for counties_dict in voting_data:
    print(counties_dict)

#county is a key
for county in range(len(voting_data)):
    print(voting_data[county]["county"])

#registered_voters is a value
for registered_voters in range(len(voting_data)):
    print(voting_data[registered_voters]["registered_voters"])

#Nested for loop
for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

for counties_dict in voting_data:
    print(counties_dict["county"])

#Multiline FString, .2f format floating decimals
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes *100:.2f}% of the total votes.")
print(message_to_candidate)