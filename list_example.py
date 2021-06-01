# list are ordered
# list items are changeable
# list allow duplicates


number_list = [5,2,3,2,1]
fruits_list = ["apple","banana","mango"]
mix_list = [1, 1.5, "list data type"]

print(number_list)
print(fruits_list)
print(mix_list)

# to find the length of the list
print(len(number_list))

## to Add elements to list
# append is used to add the elment at end of list
number_list.append(4)
print(number_list)

# to add at specific index
number_list.insert(0,6)
print(number_list)

##to remove an element from the list
# pop() is used to remove the last item in the list
# and this will return the removed element as response

# print using format method
print("number list before pop {}" .format(number_list) )
poped_element = number_list.pop()
print(poped_element)

#print using fargument
print(f"number list after pop {number_list}")

print(f"elements befor popped uisng index {number_list}")
poped_element_using_index = number_list.pop(2)
print(f"popped element using index {poped_element_using_index}")
print(f"elements after popped using index {number_list}")


# to remove the element based on string
fruits_list.append("kiwi")
print(f"elments before using remove {fruits_list}")
remove_return = fruits_list.remove("apple")
print(f"remove retun type{remove_return}")

print(f"elements after using remove { fruits_list}")

#TO REVERSE THE LIST and sort
print(f"list before sort {number_list}")
number_list.sort()
print(f"list after sort {number_list}")
number_list.reverse()
print(f"list after using reverse {number_list}")

# to clear the list
print(f"list before clear {mix_list}")
mix_list.clear()
print(f"list after clear {mix_list}")

# to delete the list
print(f"list before del {number_list}")
del number_list
# print(f"list after del {number_list}") # this will give error as we are trying to acess the deleted list


#also delete is also used to delte itme in the list using index
print(f"Before delteing {fruits_list}")
del fruits_list[0]
print(f"after del {fruits_list}")
