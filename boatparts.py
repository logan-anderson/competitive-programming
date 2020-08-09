parts, lines =  (int(i) for i in input().split())
seen = set()
for i in range(lines):
    seen.add(input())
    if len(seen) >= parts:
        print(i+1)
        exit()
print("paradox avoided")