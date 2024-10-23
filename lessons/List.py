List= [
 "name: "+input("name:"),
 "\nage: "+input("age:"),
 "\nmail: "+input("mail:")
]
print(' '.join(List))



List=[input("id one:"),input("id two:")]
for i in range(3):
 List.append(input("id"+str(i+3)+":"))
 print(List)
List.pop(2)
print(List)
