

c=int(input("How match cucumbers:"))
t=int(input("How many tomatos:"))
cola=int(input("How many cola:"))
chiken=int(input("How many chiken(KG):"))
sum=c*3+t*2+cola*5+chiken*5
print("Before tax: "+str(sum)+"\nAfter tax: "+str("%.2f" % (sum*1.17))+"\nTax:"+str("%.2f" % (sum*1.17-sum)))


