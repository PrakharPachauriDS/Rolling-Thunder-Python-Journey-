# *** Strings are immutable ***
# Means the strings cannot be changed or modified in python
# When we apply some functions on strings, python will not change the original string but make a new copy of it.

a = "SungWoo"
print(a.upper())
# Hew a new copy having upper case characters was created instead of changing the original string

print(a.lower())
print(a) # After all the operations on this string, its remains same as dit was before

# rstrip() This function will remove the trailing chracter from the string
b = "!!! Hell Yeah !!!!!!!"
print(b.rstrip("!")) #  This will not remove any characters in the starting of the string, only trailing characters
print(b)

 # replace() will replace all the occurence of a string with another string
print(b.replace("Yeah", "Noo"))


