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
