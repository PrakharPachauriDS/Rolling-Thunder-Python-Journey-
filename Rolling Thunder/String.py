# Whatever we write in "" (Double Quotes) in Python will be converted into String
Demon = "Akaza"
Opponent = "Rengoku"
print("The Winner is", Opponent)
# Single or double both can make a string in python
another_Opponent = 'Giyome'

# Suppose we want to type a sentense like He says " Come here " in python
# a = " He says "Come Here" "
# print(a)
# Surely this will give error
# *** To solve this we can either use escape sequence characters (\) or we can use single quotes and then use ""

a = 'He says "Set your heart a blaze"'
print(a)

# Multi Line String
# Triple single quotes or triple double quotes can be used to make multi line strings

b = ''' When Rengoku died,
his last words to tanjiro were
"Set your heart a blaze" '''
print(b)

# *** In python string is like array of characters ***
# And an Array can be defined a collection of items
#print(Demon[5])
# This will give us an error stating out of range

for charcter in a:
    print(a)

