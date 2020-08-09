total = input()
for i in range(int(total)):
    line = input().split()
    r1 = int(line[0])
    r2 = int(line[1]) - int(line[2])
    if r1 > r2:
        print("do not advertise")
    elif r1 < r2:
        print("advertise")
    else:
        print("does not matter")