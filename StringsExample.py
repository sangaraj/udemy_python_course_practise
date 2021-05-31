name = "Hello world"

print(name)
#spaces are also counted as char
string_length  = len(name)
print("The lenght of stirng is " + str(string_length))

#To acess the elements we can use index and index starts from zero

print("The first char of the sentence is " + name[0])
print("The last char of the sentence is " + name[string_length -1])

#we can user negative numbers to access the elements
# h e l l o
# -5 -4 -3 -2 -1
print("Accessing last char of the sentence using -ve index " + name[-1])
print("Accessing first char of the sentence using -ve index " + name[-string_length])

# start index: end index(does not include this index i.e end index -1 ) : jump numbers
print(name[0:11:1])
print(name[:11:2])
print(name[6:10:1])

print(name[1:]) # this will print from given index to last of the sentence
print(name[:7]) # this wil print form start to given index -1

print(name[::]) # this will entire string as there is not start and end index
alphabbets  = "abcefghijklmnopqrstuvwxyz"
print(name[::2]) # this will print all the alphabets by jumping one index each time

# we can use the above logic to print the letters in revere order
print(name[::-1])

#strings are immutable i.e string cant be changed
user = "pam"
# now if we want to change the letter p to m we can't by using following
# user[0] = 's'

# we can multiply stirngs
print(user*3) # this will print pam 3 times

