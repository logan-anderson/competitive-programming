
l, s1, s2 = input().split(" ")
# 𝑟 = the number of pegs that are identical in both color and position in the code and the guess
r = 0
# 𝑠 = the number of remaining pegs that are identical in color but not in the same position.
s = 0
# lets get r
colours = set()
s1Freq = {}
s2Freq = {}

for i in range(len(s1)):
    # get all the colours
    colours.add(s1[i])
    colours.add(s2[i])
    if(s1[i] not in s1Freq.keys()):
        s1Freq[s1[i]] = 0
    if(s2[i] not in s2Freq.keys()):
        s2Freq[s2[i]] = 0
    s1Freq[s1[i]] += 1
    s2Freq[s2[i]] += 1

    if(s1[i] == s2[i]):
        r += 1

# print(s1Freq)
# print(s2Freq)
for c in colours:
    x1 = 0
    try:
        x1 = s1Freq[c]
    except Exception as identifier:
        pass
    x2 = 0
    try:
        x2 = s2Freq[c]
    except Exception as identifier:
        pass

    s += min(x1, x2)
print(r, s - r)
