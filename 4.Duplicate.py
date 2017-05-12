"""This program uses a randomly generated list of 30 numbers and iterates through to check for duplicates.
If it finds a duplicate it will remove it from the list and add to a list of duplicate numbers.
At the end of the program, output will be: 
- The sorted list of random numbers
- A list of the numbers that were duplicated and
- The new list without duplicate numbers.

No input from user is required.
"""
import random
list = [ ]

while True:
    """Get a new random integer from 1 to 50"""
    rand_int = random.randint(1, 30)
    list.append(rand_int)

    if len(list) >= 30:
        """Break from the loop"""
        break
list.sort()
print("Sorted list: ", list)
newlist = [ ]
duplist = [ ]
for number in list:
    if number in newlist:
        duplist.append(number)
    elif number not in newlist:
      newlist.append(number)
print("These are the duplicate numbers: ", duplist)
print("New list without duplicates: ", newlist)
