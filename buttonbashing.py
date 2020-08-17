import sys
sys.setrecursionlimit(10000)
numTests = int(input())

for i in range(numTests):
    numberOfButtons, desiredTime = [int(i) for i in input().split()]
    buttons = [int(i) for i in input().split()]
    print(solve(buttons, desiredTime, 0, 0, 0))
    # print(numberOfButtons, desiredTime, buttons)


def solve(buttons, desiredTime: int, currentTime: int, smallestTimeAboveTarget: int, buttonPresses):
