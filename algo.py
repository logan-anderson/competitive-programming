A = [float(i) for i in input().split()]
B = [float(i) for i in input().split()]
# ab = v
# b = v/a
v = float(input())
C = set([v/a for a in A])
print(C)
for i in B:
    if i in C:
        print("YES")
