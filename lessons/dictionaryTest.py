money={}
for i in range(5):
    money[input("Name:")]=float(input("Money:"))
    print(money)


money[input("Name:")]=sum(money.values())
print(money)