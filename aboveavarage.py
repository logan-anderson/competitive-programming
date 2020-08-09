tests = int(input())
for i in range(tests):
    nums = [int(i) for i in input().split()][1:]
    average =  sum(nums) /  len(nums)
    above=0
    for i in filter(lambda x: x > average, nums):
        above= above +1
    print( '{:.3f}%'.format((above/len(nums))*100) )
