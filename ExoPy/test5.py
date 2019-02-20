import random

vm = 1000
print("lets game")
print("je pense a qu'elle nombre ? " + str(vm)+"  ?")
nbr = random.randint(1,vm)
while(True):
    nbu = int(input("alors?"));
    if(nbu > nbr):
        print("trop grand")
    elif(nbu < nbr):
        print("trop petit")
    else:
        print("Bingo")
        break
