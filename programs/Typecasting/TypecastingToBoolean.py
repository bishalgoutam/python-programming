# Developed by: Bishal Goutam
# Date: 2/1/2025

# Program starts here

# int(): converts to integer
# str(): converts to string
# float(): converts to float
# bool(): converts to boolean

# Convert Other data types to boolean
print("Typecasting to Boolean")
print("\n")
print("Typecasting Float to Boolean")
print("7.8909->",bool(7.8909))  # No rounding up to 2
print("5.7->", bool(5.7))
print("0.0->",bool(0.0))
print("\n")

print("Typecasting String to Boolean")
print("78909->",bool("78909"))  # All strings get converted to True
print("7.8909->",bool("7.8909"))  # All strings get converted to True
print("ABCD->", bool("ABCD"))   # All strings get converted to True
print("_->", bool("_"))   # All strings get converted to True
print("0->", bool("0"))   # All strings get converted to True
print("Space->", bool(" "))   # All strings get converted to True
print("Empty/Null String->", bool(""))   # Empty/Null strings get converted to False
print("\n")

print("Typecasting Integer to Boolean")
print("0->",bool(0))  # Returns false
print("1->",bool(1))    # Non-zero integers return True
print("-15->",bool(-15))
print("2345->",bool(2345))

print("\n")


# Program ends here