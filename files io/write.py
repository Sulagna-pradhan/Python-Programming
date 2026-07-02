f = open("files io/file.txt", "w")
f.write("Bokachoda")
f.close()

f = open("files io/file.txt", "r")
print(f.read())
f.close()