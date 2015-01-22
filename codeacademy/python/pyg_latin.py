pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    # process input in lower case
    word = original.lower()
    # store only the first letter
    first = word[0]
    # slice the word to only include index 1 to the length of the word
    new_word = word[1:len(new_word)] + first + pyg
    
    print new_word
else:
    print 'empty'
