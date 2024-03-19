import random

choice = input("Do you Want Play")
playernum = int()
playercolor = int()

def generate():
    generatednum = random.randint(1,1)
    generatedcolor = random.randint(3, 3)
    return generatednum, generatedcolor
    

def system(playercolor,playernum,generatednum,generatedcolor,choice):
    if choice == "yes" or "Yes":
        playernum = int(input("Choose a Number Between 1 and 36"))
        playercolor = int(input("Choose a color Black(37) or Red(38)"))

        if playernum == generatednum and playercolor == generatedcolor:
            print("you win")
        else:
            print("you lose")

        choice = input("Do you Want Play Again?")
        while choice == "yes" or "Yes":
            generatednum, generatedcolor = generate()
            system(playercolor,playernum,generatednum,generatedcolor,choice)
        else:
            return
        
generatednum, generatedcolor = generate()
system(playercolor,playernum,generatednum,generatedcolor,choice)

    
    



    



    






