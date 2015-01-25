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
