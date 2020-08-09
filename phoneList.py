tests = int(input())
for i in range(tests):
    prefs = set()
    nums = list()
    done = False
    numOfnums = int(input())
    if numOfnums == 1:
        input()
        print("YES")
        continue
    for i in range(numOfnums):
        number = input()
        prefs.add(number)
        nums.append(number)
    if not len(nums) == len(prefs):
        print("NO")
        break
    for number in nums:   
        if done:
            break    
        for i in range(len(number)+1):
            if number[:i] in prefs:
                print("NO")
                done = True
        prefs.add(number)
    if not done:
        print("YES")