def using_control_once():
    if 1 == 1:
        return "Success #1"

def using_control_again():
    if 2 % 2 == 0:
        return "Success #2"

print using_control_once()
print using_control_again()

# another example

def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)
