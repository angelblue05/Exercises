start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for number in start_list:
    square_list.append(number ** 2)

square_list.sort()
print square_list

# another example
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
    print name
    
# another example
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Print the key values
for key in webster:
    print webster[key]

# another example
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for number in a:
    if number % 2 == 0:
        print number
        
 # another example
def fizz_count(x):
    count = 0
    
    for item in x:
        if item == "fizz":
            count += 1
    
    return count

# another example - loop thru strings
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

# another example - print every item in the list
n = [3, 5, 7]
    
def print_list(x):
    for i in range(0, len(x)):
        print x[i]

print_list(n)

# another example - strings in list
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
    result = ""
    for item in words:
        result += item
    
    return result
print join_strings(n)

# another example - similar to while loop
print "Counting..."

for i in range(20):
    print i

# another example - per string, same principle
word = "eggs!"

# Your code here!
for ltr in word:
    print ltr

# another example - loop with trailing comma
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print 'X', # comma puts elements one after the each other instead of lines
    else:
        print char,

#Don't delete this print statement!
print

# another example - looping thru a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key + " " + d[key]
