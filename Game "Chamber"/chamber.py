import random
boxReward=[("green",1000),("orange",4000),("purple",9000),("gold",16000)]

chance=["chest","nothig"]
i=0
suma=0
print("Hello, it's time to start a game KOMNATA",
      "You have 5 steps in one side.Every, time you get a chance to meet one chest or nothing.Each chest contain a certain numbers of point",
      "Collects as many of them as possible. Let's go!")
print("   ")
while (i<5):
    step=input("Do you want to take a step:   ")
    if (step=="yes"):
        print("\n","Oh excellent!Let's start!")
        print("You got a ......")
        x=random.choices(chance,[60,40])[0]
        print(x)
        if (x==chance[0]):
            print("Good job, the color of chest is ...")
            tak=random.choices(boxReward,[75,20,4,1])
            print(tak[0][0])
            y=tak[0][1]
            print("You get a",y,"gold","\n")
            suma=suma+y
            print("Gongratulations! Now, you have",suma,"gold. We keep playing! ","\n")
        elif(x==chance[1]):
            print("Upss, You didn't draw any chest. Don't worry and try again","\n")
    else:
        print("I see you don't want to play anymor, so we finish")
    i+=1
print("The game is over. You scored", suma,"gold" )