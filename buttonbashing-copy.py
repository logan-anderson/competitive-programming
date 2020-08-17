import sys
sys.setrecursionlimit(10000)
numTests = int(input())


# assumes there is a solution
def solve(buttons, desiredTime: int, currentTime: int, smallestTimeAboveTarget: int, buttonPresses):
    allButtonPress = []

    if(buttonPresses > 1000):
        return [False, buttonPresses]

    if(currentTime > 60 or currentTime < 0):
        return [False, 100000000000]

    # have we gotten to the current time?
    if(desiredTime == currentTime):
        return [True, buttonPresses]
    if(currentTime >= desiredTime):
        return [False, buttonPresses]

    for button in buttons:
        # press a button
        smallestTimeAboveTarget = desiredTime - currentTime + button
        tempButtonsPresses = solve(
            buttons,
            desiredTime,
            currentTime+button,
            smallestTimeAboveTarget,
            buttonPresses + 1
        )

        allButtonPress.append(tempButtonsPresses)
    perfactButtonPresses = []
    notPerfactButtonPress = []
    print(allButtonPress)
    for [isPerfact, cButtonPressed] in allButtonPress:
        if(isPerfact):
            perfactButtonPresses.append(cButtonPressed)
        else:
            notPerfactButtonPress.append(cButtonPressed)
    if len(perfactButtonPresses) > 0:
        return [True, min(perfactButtonPresses)]
    else:
        return [False, min(notPerfactButtonPress)]


for i in range(numTests):
    numberOfButtons, desiredTime = [int(i) for i in input().split()]
    buttons = [int(i) for i in input().split()]
    print(solve(buttons, desiredTime, 0, 0, 0))
    # print(numberOfButtons, desiredTime, buttons)
