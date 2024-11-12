from time import sleep

f = "C:\\Users\\nir\\PycharmProjects\\Tests\\lessons\\MyFile.txt"
file=open(f,"r+")
print(file.read())
file.write("\nhelp\nagain")
sleep(2)
file.close
file=open(f,"r")
print(file.read())
file.close
file=open(f,"a")
file.write("\nhelp\nagain")
file.close()
file=open(f,"r")
print(file.read())
file.close()