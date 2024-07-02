#dictionaries

#empty dictionary
empty_dict = {}
empty_dict = dict()

#dictionary with initial values
my_dictionary = {"key1" : "value1", "key2" : 6353}

#getting a value 
value1 = my_dictionary["key1"]
print(value1)


#getting a value using .get 
value2 = my_dictionary.get("key2", 600)
print(value2)

#updating a value
my_dictionary["key1"] = "updated value"
print(my_dictionary)

#adding a new key, value
my_dictionary["key3"] = "new value"
print(my_dictionary)

#updating dictionary using .update

#method 1
my_dictionary.update(key2="some value", new_key="another value")
print(my_dictionary)

#method 2
my_dictionary.update([ ["key5", "value5"], ["key6", "value6"] ])
print(my_dictionary)


#deleting an item for the dictionary using the key
del my_dictionary["key2"]
print(my_dictionary)

#deleting using .pop
deleted_value = my_dictionary.pop("key3")
print(deleted_value)
print(my_dictionary)

#deleting using .popitem
deleted_key, deleted_value = my_dictionary.popitem()
print(deleted_key, deleted_value)
print(my_dictionary)

#check if a key is in a dictionary
if "key5" in my_dictionary:
    print("found", my_dictionary["key5"])


#looping through a dictionary
for key in my_dictionary:
    print(my_dictionary[key])#print value
    print(key)#print key

print("----Items(key, value)----")
for key, value in my_dictionary.items():
    print(key, value)

print("---values---")
for value in my_dictionary.values():
    print(value)


print("-"*20)
print("---WEATHER----")
weather = {
    "Abha" : 18,
    "Riyadh" : 36,
    "Addamam" : 34
    }


user_input = input("Enter City: ")
if user_input in weather:
    print(f"Temperature for {user_input} is {weather[user_input]} celsius")
else:
    print(f"Sorry we don't have the info for {user_input}")