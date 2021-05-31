# using format() method and fstring method

# 1. format methos
print("This is {}" .format("rohit") )
print("My name is {} and my age is {}" .format("rohit", 28))
print("this is {}, I live in {}" .format("rohit", "hyderabad"))
print("i learned {0}  course from {1}, paid {2} on offer " .format("python", "udemy", "385"))
print("i learned {0}  course from {1}, paid {2} on offer " .format("python", "udemy", "385"))
print("i learned {0}  course from {0}, paid {0} on offer " .format("python", "udemy", "385"))
print("i {l} {s} in {su}" .format(l = 'love', s = 'swimming', su='summer'))


#flaot formating using float method {value : width . precsion f}
#width is spacing here
result = 100/777
print("The result is {}" .format(result))
print("the result is {r:1.5f}".format(r = result))

#2. fstrig methos
name = "rohit"
age = 28
print(f"my name is {name} and my age is {age}")