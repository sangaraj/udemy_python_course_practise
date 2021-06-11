# iterating throught string
name = "mutual mobile"
for letter in name:
    print(letter)

# iterate through list to print even or odd no
my_list = [1,2,3,4,5,6,7,8,9,10]
for num in my_list:
    if num%2 == 0:
        print(f"Even no: { num}")
    else:
        print(f"odd number: {num}")

# add of all the no in the list
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for numbers in my_list:
    sum = sum + numbers
print(f"The sume of all the item in the list is {sum}")


#iterate through tuple
my_tuple = (1,2,3,4,5)
for tup_num in my_tuple:
    print(tup_num)

# we can have tuple inside the list
my_list_with_tuple = [(1,2),(3,4),(5,6)]
for list_item in my_list_with_tuple:
    print(list_item) #this will pritn tuple set
# to print the  individaul item of the tuple then we cna use concept called tuple unpacking
for a,b in my_list_with_tuple:
    print(a)
    print(b)


# iterate through dictonery
# to acess just the keys
my_dict = {'k1':1,'k2':2,'k3':3}
for dict_item in my_dict:
    print(dict_item)

#to access just the value
for dict_item in my_dict.values():
    print(dict_item)

# this will print key along with values
for dict_item in my_dict.items():
    print(dict_item)

#tuple unpacking
for key,value in my_dict.items():
    print(key)
    print(value)





