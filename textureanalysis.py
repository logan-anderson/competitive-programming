done = False
rn = 0
while not done :
    rn+=1
    line = input()
    even = True
    if line == 'END':
        done = True
        break
    whites = line[1:-1].split('*')
    current = whites[0]
    for i in whites:
        if current != i:
            even = False
            break
    if even: 
        print(rn,'EVEN')
    else:
        print(rn,'NOT EVEN')
            

