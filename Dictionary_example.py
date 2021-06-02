names = {
    "name" : "rohit",
    "age": 28,
    "weight" : 65,
    "gender" : "male"
}

print(names)

#to access the elements in dictonary
print(names["age"])

#to add elements to the dictonery
names["height"] = 5.7
print(names)

#to update element
names["name"] = "rohit kumar"
print(names)

# remove element
names.pop("height")
print(names)

# to print all key of dic
print(names.keys())

#to print all value of dic
print(names.values())

#to print all elements in form of tuples
print(names.items())

# to cleat a dic
names.clear()
print(names)

# to delete a dic
del names


school = {
    "student" :
        {
        "name" : "rohit",
        "age": 28,
        "weight" : 65,
        "gender" : "male"
        },
    "class": 10,
    "subjects": ["mpc","cec","bipc"]
}

#to print entire student feild
print(school["student"])

# to access one particular feild of stundent
print(school["student"]["name"])

print(school["class"])

print(school["subjects"])
print(school["subjects"][2])


