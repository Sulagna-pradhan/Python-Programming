d = {}
a = int(input("Enter no of elements: "))

for i in range(a):
    key = input("Enter Name: ")
    value = int(input("Enter CGPA: "))
    d[key] = value
    
print(d)

#print name

for name in d:
    parts = name.split()
    firstName = parts[0][0] +"."
    lastName = parts[-1]
    
# get highest cgps

highest_cgpa = max(d, key=d.get)
print(highest_cgpa)
print(d[highest_cgpa])
    