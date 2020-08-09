total = int(input())
for i in range(total):
    done = False
    nums = []
    totalTests = int(input())
    if totalTests == 1:
        input()
        print("YES")
        continue
    for i in range(totalTests):
        nums.append(input())
    nums.sort()
    for i in range(totalTests-1):
        if nums[i] == nums[i+1][:len(nums[i])]:
            print("NO")
            done = True
            break
    if not done:
        print("YES")
