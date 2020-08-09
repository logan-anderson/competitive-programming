words = input().split()
seen = set()
for word in words:
    start = len(seen)
    seen.add(word)
    if len(seen) == start:
        print("no")
        exit()
print("yes")
