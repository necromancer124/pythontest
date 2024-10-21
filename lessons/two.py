# l="log in pls"
# print(l)
# mail=input("enter your email: ")
# age=input("enter your age: ")
# name=input("enter your name: ")
# print("Your mail: "+mail+"Your name: \n"+name+"Your age: \n"+age)


#task one

num=input("4 digit number: ")
if(len(num)==4):
 num=int(num)
 print("thousands:"+str(num//1000)+"\nhunderds:"+str(num//100%10)+"\ntens:"+str(num//10%10)+"\nlast num:"+str(num%10))