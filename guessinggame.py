import random
jackpot = random.randint(1,100)   # here randint is the random integer from 1 to 100

guess = int(input("guess the num:"))
count = 1
while guess != jackpot:
    if  guess > jackpot:
        print("guess lower")
    else :
        print("guess higher")
    guess = int(input("guess the num:"))
    count+=1
print("correct number")        
print("you took",count,"attempts")
