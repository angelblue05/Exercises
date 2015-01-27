suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("bathing suit")
suitcase.append("sun block")
suitcase.append("book")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# another example

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =  animals.index("duck")  # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra") 

print animals # Observe what prints after the insert operation

# remove an item from a list
list.remove(item)

# another example - list of lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    
    for numbers in lists:
        for num in numbers:
            results.append(num)
    
    return results

print flatten(n)
