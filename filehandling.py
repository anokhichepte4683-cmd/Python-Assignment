#opening and writing on a file
file = open("file.txt","w")
file.write("This file is file.txt")
file.close()
#opening and reading a file
file =open("file.txt","r")
print("File contents:",file.read())
file.close()
#appending a file
file = open("file.txt","a")
file.write("The content in this file is very confidential")
file.close()
#read appended file
file =open("file.txt","r")
print("Appended File contents:",file.read())
file.close()