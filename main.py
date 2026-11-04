print(f"hej {input("vem fan e du då? ")} och välkommen till spelet!")
import random
rand_tal=random.randint(1,10)
gissning=int(input("gissa tal mellan 1-10 -->"))
if gissning == rand_tal:
    print("rätt gissning")
else:
    print(f"aj shit bro det var {rand_tal}")