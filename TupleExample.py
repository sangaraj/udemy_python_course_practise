#ordered
#allow duplicates
#immutable

mix_fruits = ("apple", "banana", "orange","mango", 1)

#tuple with single element should have , after the element
tuple_with_one_elment = ("apple",)

print(type(tuple_with_one_elment))
print(len(tuple_with_one_elment))

print(f"the first element in tuple {mix_fruits[0]}")
print(f"the last element in tuple {mix_fruits[-1]}")

print(mix_fruits[1:])
print(mix_fruits[:3])
print(mix_fruits[1:3])

# to delete tuple
del mix_fruits

"""we can add, update or remove the tuples to do so we need to conver the tuple to string to list
then perform action and then recast it to tuple

"""

