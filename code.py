#main.py

uppercase = input("Enter a word in all uppercase: ")
lowercase = ""


'''
at this point in the code, it is essential to find the end result of subtracting the uppercase from the lowecase value - use b and B as an example.
'''

difference = ord('B') - ord('b')

for i in range(0, len(uppercase)):
  letter = uppercase[i]
  lowercase += chr(ord(letter) - difference)
  

print("The word in all lowercase is: " + lowercase)
