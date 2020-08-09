# nums = input().split()
# num1 = int(nums[0])
# num2 = int(nums[1])
# outcoms = []
# prop=[]
# for i in range(num1):
#     for j in range(num2):
#         outcoms.append(i+j+2)
# for i in range(num1+num2):
#     prop.append((outcoms.count(i),i))
# prop.sort()
# highest = prop[-1][0]
# printString = '\n'.join(map(lambda a: str(a[1]) , filter(lambda a: a[0] == highest, prop)))
# print(printString)
nums = input().split()
print('\n'.join( str(i) for i in range(int(nums[0])+1,int(nums[1])+2)))