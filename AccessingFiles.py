contents = open("/Users/rohitsangaraj/Documents/Git/python/udemy_python_course_practise/myfile.txt", mode="r+")
print(contents.read())
#contents.seek(0)
print(contents.readline())

contents.write("\nhello world")
contents.seek(0)
print(contents.read())
contents.close()
