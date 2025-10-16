# Developed by: Bishal Goutam
# Date: 2/1/2025

# Program starts here

# int(): converts to integer
# str(): converts to string
# float(): converts to float
# bool(): converts to boolean

# Convert Other data types to Integer
print("Typecasting to Integer")
print("\n")
print("Typecasting float to Integer")
print("7.8909->",int(7.8909))  # No rounding up to 2
print("5.7->", int(5.7))
print("1.0->",int(1.0))
print("1.1->",int(1.1))
print("1.4->",int(1.4))
print("1.5->", int(1.5))  # No rounding up to 2
print("1.8->", int(1.8))  # No rounding up to 2
print("\n")

print("Typecasting String to Integer")
print("78909->",int("78909"))  # Within quotes only digits then it can be converted
#print("7.8909->",int("7.8909"))  # Cannot be converted
#print("ABCD->", int("ABCD"))   # Cannot be converted
print("\n")

print("Typecasting Boolean to Integer")
print("Boolean True->",int(True))
print("Boolean False->",int(False))
print("\n")


# Program ends here