A="1"
B="2"
print(A+B)
''' if you did this instead of typing numbers without double commas then you would get 12 in the place of 3
that is why we use typecasting in Python to not to make this mistake and correct it
'''
print(int(A+B))
# Nope

print(int(A)+int(B))
# Yeah
# Here what we did is convert the strings into integers first and then added them

# Implicit Typecasting (Inbuilt) (Implemented by Python)
C=12
D=3.9
print(type(C))
print(type(D))
# Here Python converted 12 into int and 3.9 into float as per data without losing any data
# So that was an example of Imlicit Typecasting
