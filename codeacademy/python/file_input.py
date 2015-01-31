# important : write-only mode ("w"), read-only mode ("r"), read and write mode ("r+"), and append mode ("a", which adds any new data you write to the file to the end of the file).

my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()

# another example - print using readline (will return one line every time you call it)
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()

# another example - implicit file closure
with open("text.txt", "w") as textfile:
	textfile.write("Success!")

# another example
with open("text.txt", "w") as my_file:
    my_file.write("I wrote to text.txt")
    
# another example - make sure the file is closed
with open("text.txt", "w") as my_file:
    my_file.write("I wrote to text.txt")

if my_file.closed == False:
    my_file.close()

print my_file.closed
