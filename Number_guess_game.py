import random
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
print(" computer has generated a number between 1-9 you have to guess the number in 5 chances")
chances=0
while chances<5:
    guess=int(input())
    if guess==number:
        print("YOU WON")
        break
    elif guess<number:
        print("HINT: you are near,guess a number above",guess)
    else:
        print("HINT: you are near but guess a number below",guess)
    chances+=1
if not chances<5:
    print("YOU LOOSE,CORRECT ANSWER WAS",number)