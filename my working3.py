# file1 = open("circus.txt")

# print(file1.read())

#print(file1.read(2)) # only return first two characters

#print(file1.read(20)) # only return first twenty characters

# print(file1.readline())  # only print first line   one line at a time
# print(file1.readline())  # only print second line

# print(file1.readlines())   # give a list of the lines making them string with \n

# while True:
#     line = file1.readline()
#     if line != "":
#         print(line)
#     else:
#         break

# lineArr = file1.readlines()
# for line in lineArr:
#     print(line)



# file1.close()

# with open("circus.txt", "r") as reader:
#     # this will automatically open and close the file no need to write open(), file.close()
#     # "r" is used to tell the file to open in reading mode
#     content = reader.readlines()  # print lines in list format
#     print(content)
#
#     print(content[::-1])  # reverse the list

#write the content of file in reversed order

# with open("circus.txt", "r") as reader:
#     content = reader.readlines()
#     print(content[::-1])
#     with open("circus.txt", "w") as writer:
#         for line in reversed(content):
#             writer.write(line)

# read the content of file

# with open("circus.txt", "r") as reader:
#     content = reader.readlines()
#     print(content)