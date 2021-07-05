#print("Hello World")

#formula=(5 + 2 * 3)
#print ("5 + 2 * 3= "  + str(formula))
#formula2=8 // 5 - 3
#print ("8 // 5 - 3=" + str(formula2))
#formula3=8 + 22 * 2 - 4
#print ("8 + 22 * 2 - 4=" + str(formula3))
#formula4=16 - 3 / 2 + 7 - 1
#print ("16 - 3 / 2 + 7 - 1=" + str(formula4))
#formula5=3 ** 3 % 5
#print ("3 ** 3 % 5=" + str(formula5))
#formula6=5 + 9 * 3 / 2 - 4
#print ("5 + 9 * 3 / 2 - 4=" + str(formula6))

#counties = ["Arapahoe","Denver","Jefferson"]
#counties.insert("El Paso")
#counties.remove("Arapahoe")

#print(counties[2])

#print(counties[0:3])
#counties.append("El Paso")
#counties.insert(2,"El Paso")
#print(counties)
#counties.remove("El Paso")
#print(counties)

#counties.pop(3)
#print(counties)
#counties[2] = "El Paso"
#print(counties)

#counties_tuple = ("Arapahoe","Denver","Jefferson")
#len(counties_tuple)

#counties_dict = {}
#counties_dict["Arapahoe"] = 422829
#print(counties_dict)
#counties_dict["Denver"] = 463353
#counties_dict["Jefferson"] = 432438
#print(counties_dict)
#print(len(counties_dict))
#counties_dict.items()
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#print(voting_data)
#voting_data.insert(1,{'county':'El Paso','registered_voters':422829})
#voting_data.remove({'county': 'Arapahoe', 'registered_voters': 422829})
#print(voting_data)

# How many votes did you get?
#my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

counties = ["Arapahoe","Denver","Jefferson"]
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Both Arapahoe and El Paso are not in the list of counties.")#

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")
#count = 7

#while count < 1:

#    print("Hello World")

#for num in range(len(counties)):
#    print(counties[num])

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:
#    print(county_dict)
#for county in range(len(voting_data)):

 #     print(voting_data[county]['county'])



for county_dict in voting_data:

     print(county_dict['registered_voters'])

