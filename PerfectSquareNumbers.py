from math import sqrt

Root = 0

for i in range(1,500):
    root = sqrt(i)
    if root == int(root):
        print(i)