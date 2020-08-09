done = False
while not done:
    graph = []
    while True:
        try:
            inStuff = input()
        except EOFError:
            done = True
            break
        if inStuff == '':
            break
        graph.append(inStuff)
    stars = 0
    # graph.reverse()
    for i in graph:
        current = i.count('*')
        print( ''.join(['.' for i in range(len(i) - stars - current)]) + ''.join(['*' for i in range(current)])  + ''.join(['.' for i in range(stars)]) )
        stars = stars + current
    print()

