import random
import math
print("you have $50 and you go to a roulette table")
choice = input("Do you Want To Play?")
playernum = int()
playercolor = ("")
moneytotal = 50
moneynum = int()
betchoice = int()
turns = []

def generate():
    generatednum = random.randint(1,36)
    generatedcolor = random.choice(["red", "black"])
    
    return generatednum, generatedcolor
    

def system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice,turns):
    if moneytotal > 0:
        if choice == "yes" or choice == "Yes":
            betchoice = int(input("Do you want to bet color & number(1), or just color(2)"))
            moneynum = int(input("How much do you want to bet?"))
            moneytotal = moneytotal - moneynum
       

            if betchoice == 1:
                playernum = int(input("Choose a Number Between 1 and 36"))
                playercolor = (input("Choose a color Black or Red"))
                if playernum == generatednum and playercolor == generatedcolor:
                    print("you win")
                    print("it was", generatednum,generatedcolor)
                    moneytotal = math.ceil(moneytotal + 2*moneynum)
                    print("your new total is", moneytotal)
                    print("$",moneytotal)

                if playercolor == generatedcolor:
                    moneytotal = math.floor(moneytotal + moneynum/2)
                    print("you only got the color right")
                    print("your new total is","$", moneytotal)
                else:
                    print("you lose")
                    print("it was" ,generatednum,generatedcolor)
                    print("your new total is","$", moneytotal)

            if betchoice == 2:
                playercolor = (input("Choose a color, Black or Red"))
                if playercolor == generatedcolor:
                    moneytotal = math.ceil(moneytotal + 1.5*moneynum)
                    print("you got it right")
                    print("it was" ,generatedcolor)
                    print("your new total is","$", moneytotal)
                else:
                    print("you got it wrong")
                    print("it was" ,generatedcolor)
                    print("your new total is","$", moneytotal)


            choice = input("Do you Want Play To Again?")
            if choice == "yes" or choice == "Yes":
                turns.append(generatednum)
                turns.append(generatedcolor)
                print(turns)
                generatednum, generatedcolor = generate()
                system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice,turns)
            else:
                print("Thank you for playing")
                print("*you walk out the casino with*","$",moneytotal)
        else:
            print("*you exit the casino*")
        
    else:
        print("you have been kicked out from the casino for trying to play without money.")
        
generatednum, generatedcolor = generate()
system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice,turns)

    
    



    



    






