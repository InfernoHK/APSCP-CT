import random

playernum = input("Choose a Number Between 1 and 36")
playercolor = input("Choose a color Black(37) or Red(38)")

def generate():
    generatednum = random.randint(1,36)
    generatedcolor = random.randint(37, 38)
    
    

def system(playercolor,playernum,generatednum,generatedcolor):
    if (playercolor == generatedcolor) and (playernum == generatednum):
        print("you win")
    else:
        print("you lose")

    system()
    


    



    






