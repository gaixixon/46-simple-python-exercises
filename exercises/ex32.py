"""Write a version of a palindrome recogniser that accepts a file name 
from the user, reads each line, and prints the line to the screen if it 
is a palindrome."""

# Solution by Nick Rameau - @R4meau
import string

file_name = raw_input('Enter the file name> ')
punctuation = string.punctuation + ' '

def is_palindrome(str):
  new_str = filter(lambda x: x not in punctuation, str.lower())
  if new_str == new_str[::-1]:
    return True

with open(file_name, 'r') as f:
  for line in f:
    # Here I used rstrip to remove the newline (\n) at the end of the line
    if is_palindrome(line.rstrip()):
      print line.rstrip()
  

# Solution by Your Name - @YourUsername
# You can add your solution here.
# A good way to show other people your solution
# to this exercise. Remember to comment it out.
# I'll be waiting for your pull request.
# And please, leave this comment block intact so other people
# Can see it later too.