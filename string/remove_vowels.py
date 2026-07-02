str1 = str(input("Enter Your String: ")).lower()
vowels = 0

for ch in str1: 
    if ch  in ("aeiou"):
        new = new+ch
print(new)
