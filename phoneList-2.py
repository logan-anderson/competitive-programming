tests = int(input())
for i in range(tests):
    nums = list()
    done = False
    numOfnums = int(input())
    if numOfnums == 1:
        input()
        print("YES")
        continue
    for i in range(numOfnums):
        number = input()
        nums.append(number)
    nums.sort()
    # print(nums)
    for i in range(numOfnums-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            print("NO")
            done = True
            continue

    if not done:
        print("YES")