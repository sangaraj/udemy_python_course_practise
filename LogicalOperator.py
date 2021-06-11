# logical operator are:
# and
# or
# not

a = 10
b = 20
c = 5

#logical and : it will return true only if both condions are true
print( a > b and c > b)
print(a < b and b > c)

#logical or this will return true if any of the contion among two returns true
print( a > b or c < b)
print(a < b or b > c)
print(a > b or b < c)

#not this will send the opposite of result
value_true =  True
value_false = False

print(not value_false)
print(not value_true)