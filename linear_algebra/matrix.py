import numpy as np

dimention1 = int(input("Enter Dimention of u vector: "))
for i in range(dimention1):
    u = list(map(int, input().split()))

dimention2 = int(input("Enter Dimention of v vector: "))
for i in range(dimention2):
    v = list(map(int, input().split()))
    
    
a = np.array(u)
b = np.array(v)

print(a)

    