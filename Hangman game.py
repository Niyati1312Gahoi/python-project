import random as r
def hang(a):
    if a==0:
        print('''
             +------+ 
             O      |
                    |
                    |
                    |
                +=======+
''')
    if a==1:
        print('''
             +------+ 
             O      |
             |      |
                    |
                    |
                +=======+
''')
    if a==2:
        print('''
             +------+ 
             O      |
            /|      |
                    |
                    |
                +=======+
''')
    if a==3:
        print('''
             +------+ 
             O      |
            /|\     |
                    |
                    |
                +=======+
''')
    if a==4:
        print('''
             +------+ 
             O      |
            /|\     |
            /       |
                    |
                +=======+
''')
    if a==5:
        print('''
             +------+ 
             O      |
            /|\     |
            / \     |
                    |
                +=======+
''')

def hangmangame():
    s=("fox","rocket","cat","table","laser","computer","python","maths","straw")
    print("------------------- Greetings !! -----------------")
    ch=input("READY TO PLAY THE GAME\nEnter Yes or No : ").capitalize()
    if ch=="Yes":
        a=r.choice(s)
        m=r.randint(0,len(a))
        n=r.randint(0,len(a))
        k=[]
        for i in range (len(a)):
            if i==m:
                print(a[i],end='')
                k.append(a[i])
            elif i==n:
                print(a[i],end='')
                k.append(a[i])
            else:
                print("_",end='')
                k.append("_")
        print()
        ms=[]
        c=0
        while True:
            b=input("Enter the missing alphabet : ").lower()
            if b in a:
                ct=0
                for i in range (len(a)):
                    if b==a[i]:
                        ct=i
                k[ct]=a[ct]
                print(k)
                hang(c)
                if k==list(a):
                    print("---------------Hurray! you have guessed it")
                    break
            else:
                c=c+1
                ms.append(b)
                print("Missed letters : ",ms)
                print(k)
                hang(c)
                if c==5:
                    print("Correct answer is : ",a.capitalize(),"\n-------------- Better Luck Next Time")
                if k==list(a):
                    print("--------------- Hurray! you have guessed it")
                    break
    rec=input("Do you want to play again ( Yes or No ) : ").capitalize()
    if rec=="Yes":
        hangmangame()
hangmangame()
