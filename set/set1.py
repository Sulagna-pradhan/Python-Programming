a = set(map(int, input("Enter numbers: ").split()))
b = set(map(int, input("Enter numbers: ").split()))

print("Union: ", a | b)
print("Intersection: ", a & b)
print(a ^ b)
