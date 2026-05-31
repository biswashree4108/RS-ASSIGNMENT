a = input("Enter first string: ").lower()
b = input("Enter second string: ").lower()

if sorted(a) == sorted(b):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")