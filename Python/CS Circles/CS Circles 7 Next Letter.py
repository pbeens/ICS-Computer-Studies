'''
From http://cscircles.cemc.uwaterloo.ca/7a-strings/

Write a program that takes a character as input (a string of length 1), which you should assume is an upper-case
character; the output should be the next character in the alphabet. If the input is 'Z', your output should be 'A'.

Note: this program does account for the letter Z! What approach might you take to fix this?
'''

# prompt for a letter and make it uppercase
letter = input('Enter a letter: ').upper()

# what is the ordinal value of the letter?
print ('The ordinal value of', letter, 'is', ord(letter))

# what is the ordinal value of the NEXT letter (so we can get the chr() of it)
ord_of_next_letter = ord(letter) + 1

# output the chr() of the ordinal of the next letter
print ('The next letter is', chr(ord_of_next_letter))

