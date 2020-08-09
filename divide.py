def getRidOfTrailing(num):
    found = False
    i = len(num) -1
    while True:
        if num[i] == '.':
            return i
        if num[i] != '0':
            return i + 1
        i = i -1
    return i

num =  input()
demo = input()

size = len(num)
dec = len(demo) -1
if size <= dec:
    print('0.'+ ''.join('0' for i in range(dec-size))  + num)
    exit()
num = num[:size-dec] + '.' + num[size-dec:]
cut = getRidOfTrailing(num)
print(num[:cut])

print(hex(int(input(),8)))