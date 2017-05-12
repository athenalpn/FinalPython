"""Using the random module, generates two positive one-digit numbers.
Displays a question to the user incorporating those numbers, e.g. “What is the sum of x and y?”.
Uses random to generate +, -, or * as the operators.
Conducts error-checking on the answer and notifies the user whether the answer is correct or not.
At the end gives a running total, e.g. "You got 10 out of 10"

You will do the math as asked and input the answer. If you are wrong you will be told that is incorrect, 
if you are right, you will be told as such. At the end of the quiz, you will getting a running total of correct answers.
"""

import random
from operator import add, sub, mul

name = input("What is your name? ")
print("Hello, {}. You will be completing a quiz that will ask you 10 questions which will test you on adding, subtracting and multiplying two numbers together.".format(name))

score = 0
for count in range(10):
    ops = {'+': add, '-': sub, 'x': mul}
    op = random.choice(list(ops.keys()))
    x = random.randint(1,9)
    y = random.randint(1,9)

    print("What is {} {} {}? ".format(x, op, y))
    question = int(input())
    answer = ops[op](x,y)
    if question == answer:
        print("Well done, this is correct!")
        score += 1
    else:
        print("Sorry, but this is incorrect.")

print("Well done {}! You have completed the quiz. Your final score {} out of 10.".format(name, score))