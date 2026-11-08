str1 = "Sulagna Pradhan"

# remove space with hiphen
str2 = str1.replace(" ", "-")

# remove all white space
str3 = str1.replace(" ", "")


print(str2)
print(str3)

# print string in reverse
print(str1[::-1])

# print last n characters
# we can take value of n from users but we assume 
n = 4
print(str1[-n:])