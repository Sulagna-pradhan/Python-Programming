with open("files io/file.txt", "w") as f:
    f.write("Bokachoda")

with open("files io/file.txt", "r") as f:
    print(f.read())