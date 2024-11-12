


friends=["anton","samadra","dracula"]


def friendsList(x):
    x=x.lower()
    if "none" in x:
     for x in friends:
        print("friend:"+x)
    else:
        friends.append(x)
        for x in friends:
            print("friend:"+x)
    pass
def dogDitails():

    print("Dog Name: anton")
    print("Dog size: 25 cm")
    print("Dog color: blue")
    print("Dog food: rats")
    pass




def NAzzeret(x):
    x=int(x)

    num=1
    for i in range(1,x):
        num=num*i
    print(num)







def menu(x):
    x=int(x)
    if(x==1):
        friendsList(input("write a friend or None:"))
    if(x == 2):
        dogDitails()

    if x == 3:
     NAzzeret(input("Number:"))
pass
#############################MAINMAINMAINMAINMAINMAIN###########################################


while True:
 menu(input("a number"))