#unordered
# no duplicates
# unchangeable i.e we can add item but we cant change already added item in the set

myset = {"srk", 1, 1.5, "mango"}
print(myset)

myset.add("apple")
print(myset)

# to delete the item, if item does not exists then this method will raise an error
myset.remove("srk")
print(myset)

#if item does not exists then this method will not raise an error
myset.discard(1)
print(myset)

myset.pop() # this will remove the last item in the list,
print(myset)

list5 = [1,2,2,33,4,4,11,22,3,3,2]
list5 = set(list5)
print(list5)
print(list(list5))