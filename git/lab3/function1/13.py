import random
print("Hello! What is your name?")
name = str(input())
print(f"Well, {name}, I am thinking of a number between 1 and 20 \nTake a guess")
tr = True
answer = random.randint(1, 20)
numtry = 0
while(tr):
    num = int(input())
    numtry +=1
    if(num > answer):
        print("Your guess is too high \nTake a guess")
    elif(num < answer):
        print("Your guess is too low \nTake a guess")
    if(num == answer):
        tr = False
print(f"Good job,{name}! You guessed my number in {numtry} guesses!")

