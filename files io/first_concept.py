# Types of files 
# Text Files: .txt, .docx etc

# Major operation is - read & write data | open files | close files etc

f = open("files io/file.txt", "r")
data = f.read()
print(data)
f.close()