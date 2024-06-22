Rengoku = "Set your heart a blaze"
print(len(Rengoku))
# *** The len function will let us know the length of a string

print(Rengoku[0:11])
# Here we are implementing string slicing by stating the start and end of the string

# *** We use () for functions and [] for slicing
 # Some Defaults in Python
print(Rengoku[0:15]) # Normal case, will print from 1-14 excluding 15th term
# Including 0 not 15
print(Rengoku[:11]) # Python will add 0 as default if you leave it blank
print(Rengoku[1:]) # Python will add length of string as default in the end

# Negative Slicing
print(Rengoku[-10:-5])
print(Rengoku[len(Rengoku)-10:len(Rengoku)-5])
# These both means the same in python
        


