# Developed by: Bishal Goutam
# Date: 2/1/2025

# Program starts here
# print, concatenate, replication,
# print string
print("A")
print('A')
print("Hello Python! This is one line string.")
print("Hello Python! This is two line string.\nThis is second line")

# concatenate string using + and comma
print("String 1" + "String 2")  # Concatenating with + no extra space is added in between the strings
print("String 1","String 2")    # Concatenating with , an extra space is added in between the strings

# string replication using integer/count multiplication
print("String One " * 3)
# pattern 1
print("*" * 1)
print("*" * 2)
print("*" * 3)
print("*" * 4)
print("*" * 5)
# pattern 2
print(" "*5 + "*"*1)
print(" "*4 + "*"*2)
print(" "*3 + "*"*3)
print(" "*2 + "*"*4)
print(" "*1 + "*"*5)

# Check string length using len() function
print(len("Word"))   # =4
print(len("This is a sentence."))  # =19

# String indexes
name = "clear"
ln = len(name)
print(name[0])  #c
print(name[1])  #l
print(name[2])  #e
print(name[3])  #a
print(name[4])  #r
print("\n")
print(name[-1]) #r
print(name[-2]) #a
print(name[-3]) #e
print(name[-4]) #l
print(name[-5]) #c
print("\n")
print(name[-5]) #c
print(name[-4]) #l
print(name[-3]) #e
print(name[-2]) #a
print(name[-1]) #r
print("\n")
print(name[-ln]) #c
print(name[-ln+1]) #l
print(name[-ln+2]) #e
print(name[-ln+3]) #a
print(name[-ln+4]) #r

# String slicing
print(name[0:5]) # 0 to 5-1
print(name[1:5]) # 1 to 5-1
print(name[2:5]) # 2 to 5-1
print(name[3:5]) # 3 to 5-1
print(name[4:5]) # 4 to 5-1
print(name[0:5]) # 0 to 5-1
print(name[0:4]) # 0 to 4-1
print(name[0:3]) # 0 to 3-1
print(name[0:2]) # 0 to 2-1
print(name[0:1]) # 0 to 1-1
print(name[0:0]) # 0 to 0-1  # Nothing gets printed. No error

print(name[0:]) # 0 to last
print(name[1:]) # 1 to last
print(name[2:]) # 2 to last
print(name[3:]) # 3 to last
print(name[4:]) # 4 to last
print(name[:5]) # 0 to 5-1
print(name[:4]) # 0 to 4-1
print(name[:3]) # 0 to 3-1
print(name[:2]) # 0 to 2-1
print(name[:1]) # 0 to 1-1
print(name[:0]) # 0 to 0-1  # Nothing gets printed. No error


print(name[-5:-1])
print(name[-5:-2])
print(name[-5:-3])
print(name[-5:-4])

# Case
print(name)
print(name.lower())  # All lower
print(name.upper())  # All upper

# String Manipulations strip, replace, count, find
new_name = " Clear   Glass "
print(new_name)
print(new_name.strip())
print(new_name.replace("clear","white"))  #case sensitive search. "clear" is not found
print(new_name.replace("Clear","white"))
print(new_name.count("e"))
print(new_name.count("a"))
print(new_name.count("ear"))
print(new_name.find("r"))
print(new_name.find("b"))   #not found
# Program ends here