str1 = "Sulagna".lower()

vowels = ["a", "e", "i", "o", "u"]

for ch in str1:
    if ch in vowels:
        print(ch, "is a vowel")
    else:
        print(ch, "is not a vowel")