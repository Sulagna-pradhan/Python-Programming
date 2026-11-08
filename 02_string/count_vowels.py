str1 = str(input("Enter string: ")).lower()
vowels = 0
consonent = 0

for ch in str1: 
    if ch in ("aeiou"):
        vowels+=1
    if ch not in ("aeiou"):
        consonent+=1
print(vowels)
print(consonent)