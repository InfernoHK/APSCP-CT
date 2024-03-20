import random

choice = input("Do you Want Play")
playernum = int()
playercolor = int()
moneytotal = 50
moneynum = int()
betchoice = int()
def generate():
    generatednum = random.randint(1,36)
    generatedcolor = random.randint(37, 38)
    
    return generatednum, generatedcolor
    

def system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice):
    if moneytotal > 0:
        
        

        if choice == "yes" or choice == "Yes":
            betchoice = int(input("Do you want to bet color & number(1) or just color (2)"))
            moneynum = int(input("How much do you want to bet"))
            moneytotal = moneytotal - moneynum
       

            if betchoice == 1:
                playernum = int(input("Choose a Number Between 1 and 36"))
                playercolor = int(input("Choose a color Black(37) or Red(38)"))
                if playernum == generatednum and playercolor == generatedcolor:
                    print("you win")
                    print("it was", generatednum,generatedcolor)
                    moneytotal = moneytotal + 2*moneynum
                    print("your new total is", moneytotal)
                    print(moneytotal)

                if playercolor == generatedcolor:
                    moneytotal = moneytotal + moneynum/2
                    print("you only got the color right")
                    print("your new total is", moneytotal)
                else:
                    print("you lose")
                    print("it was" ,generatednum,generatedcolor)
                    print("your new total is", moneytotal)

            if betchoice == 2:
                playercolor = int(input("Choose a color Black(37) or Red(38)"))
                if playercolor == generatedcolor:
                    moneytotal = moneytotal + 1.5*moneynum
                    print("you got it right")
                    print("it was" ,generatedcolor)
                    print("your new total is", moneytotal)
                else:
                    print("you got it wrong")
                    print("it was" ,generatedcolor)
                    print("your new total is", moneytotal)


            choice = input("Do you Want Play Again?")
            if choice == "yes" or choice == "Yes":
                generatednum, generatedcolor = generate()
                system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)
            else:
                print("Thank you for playing")
        else:
            print("Loser")
    else:
        print("you have been kicked out from the casino bum")



        


generatednum, generatedcolor = generate()
system(playercolor,playernum,generatednum,generatedcolor,choice,moneynum,moneytotal,betchoice)

    
    



    



    






