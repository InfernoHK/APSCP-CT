import random

playernum = input("Choose a Number Between 1 and 36")
playercolor = input("Choose a color Black(37) or Red(38)")

def generate():
    generatednum = random.randint(1,1)
    generatedcolor = random.randint(3, 3)
    print(generatednum)
    print(generatedcolor)
    
    
    

def system(playercolor,playernum,generatednum,generatedcolor):
    if (playernum == generatednum) and (playercolor == generatedcolor):
        print("you win")

    else:
        print("you lose")
    


generate()
system('playercolor','playernum','generatednum','generatedcolor')
    



    






