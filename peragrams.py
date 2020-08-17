inThing = input()
wordFreq = dict()
for i in inThing:
    if i in wordFreq:
        wordFreq[i] += 1
    else:
        wordFreq[i] = 1
oddc = 0
for i in wordFreq:
    if wordFreq[i] % 2 == 1:
        oddc += 1
if oddc <= 1:
    print(0)
else:
    print(oddc-1)
