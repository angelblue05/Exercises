num = 1

while num < 11:  # Fill in the condition
    # Print num squared
    print num * num
    # Increment num (make sure to do this!)
    num += 1
    
# another example
choice = raw_input('Enjoying the course? (y/n)')

while choice != "y" and choice != "n":  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
    
# another example
count = 0

while count < 10: # Add a colon
    print count
    # Increment count
    count += 1

# another example
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
        
# another example
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"

# another example - guessing game
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        
        break
    
    guesses_left -= 1
else:
    print "You lose."
