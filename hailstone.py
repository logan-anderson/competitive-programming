# hailstone
def solve(current, thesum):
    if(current == 1):
        return 1 + thesum
    if(current % 2 == 0):
        return solve(current//2, current + thesum)
    else:
        return solve(3*current + 1, current + thesum)


print(solve(int(input()), 0))
