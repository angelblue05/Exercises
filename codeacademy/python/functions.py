def one_good_turn(n):
    return n + 1
    
def deserves_another(n):
    return one_good_turn(n) + 2
    
# another example

def cube(number):
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

# another example

def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"
