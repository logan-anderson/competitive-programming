nums = [int(i) for i in input().split()]
nums.sort()
leters = [i for i in input()]
allstuff = {'A': nums[0], 'B': nums[1], 'C': nums[2]}

newString = ''
for i in leters:
    newString = newString +  str(allstuff[i]) + " "
print(newString)