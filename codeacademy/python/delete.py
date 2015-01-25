n = [1, 3, 5]
n.pop(1)
# Returns 3 (the item at index 1)
print n
# prints [1, 5]

 # another example
 
n.remove(1)
# Removes 1 from the list,
# NOT the item at index 1
print n
# prints [3, 5]

# another example

del(n[1])
# Doesn't return anything
print n
# prints [1, 5]
