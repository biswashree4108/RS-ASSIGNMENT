from math import gcd

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

g = gcd(a, b)
l = (a * b) // g

print("GCD =", g)
print("LCM =", l)
