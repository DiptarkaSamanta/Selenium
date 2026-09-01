string = "my Hero is: Spiderman1"
string2 = "helpJokers@yahoo.in"
string3 = "Itachi is the greatest Uchiha!"
string4 = "is"
string5 = "           Save your nuts my queen.    "
string6 = "madara, naruto, kakashi"

print(string + " and " + string3)

print(string2[2])
print(string2[:3])  # explicit
print(string2[0:4]) #substrings
print(string2[-3:])
print(string2[::2])
print(string2[::-1])
print(string2[4:])

res = "".join(string3.split())
print(res)

res2 = "$__$".join(string3.split())
print(res2)

print(string4 in string)  # substring cheaking

arr = string.split()
print(arr)

arr2 = string.split(":")
print(arr2)

print(string5.strip())     #  trim the head and tail white spaces
print(string5.lstrip())    #  trim the left white spaces
print(string5.rstrip())    #  trim the right white spaces

arr3 = string5.strip().split(" ")
print(arr3)

arr4 = string6.split(",")
print(arr4)
for word in arr4:
    print(word.strip())

arr5 = [word.strip() for word in string6.split(",")]
print(arr5)

print(string.index("H"))
print(string.index("i")) # first occurrance
#      print(string.index("h"))  #  give error as no index hold "h"

print(string.find("H"))  # find give first occurrance also
print(string.find("h"))  # find return -1 if not found the character "h"

