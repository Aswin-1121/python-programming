newFile = open("content.txt","a")
newFile.write("i am iron man \n")
newFile.close()

readFile = open("content.txt","r")
print(readFile.readlines())
readFile.close()
