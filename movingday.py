i, di = input().split(" ")
vals = []
for i in range(int(i)):
    l, w, h = [int(i) for i in input().split(" ")]
    vals.append(l*w*h)
print(max(vals) - int(di))
