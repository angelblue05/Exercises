# anonymous function
lambda x: x % 3 == 0

# is the same as
def by_three(x):
    return x % 3 == 0
    
    
# another example
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

# another example
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x is "Python", languages)

# another example
squares = [x * x for x in range(1, 11)]
print filter(lambda x: x in range(30, 71), squares)
