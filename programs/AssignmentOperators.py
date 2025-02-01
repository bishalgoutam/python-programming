# Developed by: Bishal Goutam
# Date: 1/31/2025

# Program starts here

print("Assignment Operations on Integers")
x = 5
x += 3  # Same as x = x + 3
print("x += 3:", x)

x -= 2  # Same as x = x - 2
print("x -= 2:", x)

x *= 4
print("x *= 4:", x)

x /= 2
print("x /= 2:", x)

x //= 2
print("x //= 2:", x)

x %= 3
print("x %= 3:", x)

x **= 2
print("x **= 2:", x)
print("\n")

print("Assignment Operations on Float")
x = 5.5
x += 3.5  # Same as x = x + 3.5
print("x += 3.5:", x)

x -= 2.3  # Same as x = x - 2.3
print("x -= 2.3:", x)

x *= 4.7
print("x *= 4.7:", x)

x /= 2.3
print("x /= 2.3:", x)

x //= 2.2
print("x //= 2.5:", x)

x %= 3.3
print("x %= 3.3:", x)

x **= 2.1
print("x **= 2.1:", x)
print("\n")


print("Assignment Operations on Boolean")
x = True
x += True  # Same as x = x + 1
print("x += True:", x)

x -= False  # Same as x = x - 0
print("x -= False:", x)

x *= True
print("x *= True:", x)  # Same as x = x * 1

x /= True
print("x /= True:", x)  # Same as x = x / 1. A division by False ends the script execution without any error.

x //= True
print("x //= True:", x)  # Same as x = x//1. Returns quotient

x %= True
print("x %= True:", x)  # Same as x = x//1. Returns remainder

x **= True
print("x **= True:", x)

x *= False
print("x *= False:", x)  # Same as x = x * 0

print("\n")
# Program ends here