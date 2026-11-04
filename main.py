print(f"hej {input("vem fan e du då? ")} och välkommen till spelet!")
import random
rand_tal=random.randint(1,10)
rätt=False
for i in range(3):
    gissning=int(input("gissa tal mellan 1-10 -->"))
    if gissning == rand_tal:
        print("rätt gissning")
        rätt=True
        break
    if i != 2:
        print(f"nuh-uh! {2-i} gissningar kvar")
if not rätt:
    print(f"aj shit bro det var {rand_tal}")