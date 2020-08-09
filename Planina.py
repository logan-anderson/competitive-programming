# unfinished
n = int(input())
total = 9
for i in range(1,16):
    print(i)
    if i == n:
        print(total)
        exit()
    else:
        total = (total**.5 + i+1)**2