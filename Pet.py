max_index = 0
max_score = 0
for i in range(5):
    current = sum(int(i) for i in input().split() )
    if current > max_score:
        max_score = current
        max_index = i + 1
print(max_index, max_score)
