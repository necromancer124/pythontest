List={"name: "+input("name:"),"\nage: "+input("age:"),"\nmail: "+input("mail:")}
print(' '.join(List))
List={input("id one:"),input("id two:")}
for i in range(3):
 List.add(input("id"+str(i+3)+":"))
 print(List)