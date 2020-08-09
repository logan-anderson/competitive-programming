from math import gcd 
def getLCM():
    allStuff = input().split()
    nums = []
    for i in allStuff:
        nums.append(int(i))
    lcm = nums[0]
    for i in nums[1:]:
        lcm = lcm*i // gcd(lcm, i)
    print(lcm)

while True:
    try:
        getLCM()
    except EOFError:
        exit()