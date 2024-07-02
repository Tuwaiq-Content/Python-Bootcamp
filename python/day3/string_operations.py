#String Operations

favorite_team:str = "Manchester United"
league:str = "Premeir League"

#accessing a single character
print(favorite_team[3])

#accessing a single character from the end
print(league[-3])

#accessing a range of characters (Slicing)
#in ranges the start is inclusive, the end is exclusive
print(league[0:4])
print(league[4:])
print(league[:])
print(league[0:7:2]) #step size


#upper
print(favorite_team.upper())
print(favorite_team.count("United"))
print(favorite_team.startswith("M"))


#formatting string / String interpolation / Concatination

#Concatination
phrase = "My favorite team is " + favorite_team + " which plays in the " + league
print(phrase)

phrase = "My favorite team is {} which plays in the {}".format(favorite_team, league)
print(phrase)

phrase = f"My favorite team is {favorite_team} which plays in the {league}"
print(phrase)

