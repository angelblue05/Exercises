print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

one =    0b1
two =    0b10
three =  0b11
four =   0b100
five =   0b101
six =    0b110
seven =  0b111
eight =  0b1000
nine =   0b1001
ten =    0b1010
eleven = 0b1011
twelve = 0b1100v

# convert a number into bitwise
print bin(1)

# another example - convert back into integer
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print int("11001001",2)

# another example
shift_right = 0b1100
shift_left = 0b1

# Your code here!
shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

# another example
     a:   00101010   42
     b:   00001111   15       
===================
 a & b:   00001010   10

# another example
     a:  00101010  42
     b:  00001111  15       
================
a | b:  00101111  47

# another example
    a:  00101010   42
    b:  00001111   15       
================
a ^ b:  00100101   37

# another example
a =    0b10111011
mask = 0b00000100
print bin(a | mask)

# another example
def check_bit4(input):
    mask = 0b1000
    compared = input & mask
    if compared > 0:
        return "on"
    else:
        return "off"

# another example
a = 0b11101110
mask = 0b11111111
print bin(a ^ mask)

# another example - slip on a mark
def flip_bit(number, n):
    mask = 0b1 << n - 1
    result = number ^ mask
    return bin(result)
