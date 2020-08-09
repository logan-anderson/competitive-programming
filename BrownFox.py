total = int(input())
alph = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

for i in range(0, total):
    notseen =''
    s = input().lower()
    for i in alph:
        if not (i in s):
            notseen = notseen + i
    if notseen == '':
        print('pangram')
    else:
        print('missing',notseen)