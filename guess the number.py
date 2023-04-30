# GUESS THE NUMBER
# GUESS THE NUMBER
import random
print("********Welcome to the GUESS THE NUMBER GAME!********\n")
level=int(input("1-Easy\n2-Medium\n3-Hard\nEnter the level number:"))
score=0
if(level==1):
    start=int(input("\nEnter the starting value:"))
    end=int(input("\nEnter the ending value:"))
    n=random.randrange(start,end)
    while(True):
        num=int(input(f"\nEnter the number you guessed in range ({start}-{end}):"))
        if(n==num):
            print("\nYou guessed it right Woaahh!")
            score+=1
            break
        elif(num<n):
            print("\nYou guessed a smaller number!")
        else:
            print("\nYou guessed a large number!")
        score+=1
    print("\nYour score is:",score)
elif(level==2):
    n=random.randrange(100,300)
    attempts=10
    print(f"\nYou have {attempts} attempts to guess the number!")
    fail=1
    while(attempts):
        num=int(input("\nEnter the number you guessed in range (100-300):"))
        if(n==num):
            print("\nYou guessed it right Woaahh!")
            score+=1
            attempts-=1
            fail=0
            break
        elif(num<n):
            print("\nYou guessed a smaller number!")
            fail=1
        else:
            print("\nYou guessed a large number!")
            fail=1
        score+=1
        attempts-=1
    if(fail==1):
        print("\nYour attempts are finished!")
        score=0
    print("\nYour score is:",score)
else:
    n=random.randrange(100,1000)
    attempts=5
    print(f"\nYou have {attempts} attempts to guess the number!")
    fail=1
    while(attempts):
        num=int(input(f"\nEnter the number you guessed in range (100-1000):"))
        if(n==num):
            print("\nYou guessed it right Woaahh!")
            score+=1
            attempts-=1
            fail=0
            break
        elif(num<n):
            print("\nYou guessed a smaller number!")
            fail=1
        else:
            print("\nYou guessed a large number!")
            fail=1
        score+=1
        attempts-=1
    if(fail==1):
        print("\nYour attempts are finished!")
        score=0
    print("\nYour score is:",score)
