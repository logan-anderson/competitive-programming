height, width, numberOfBricks = [int(i) for i in input().split(" ")]
bricks = [int(i) for i in input().split(" ")]
# bricks.sort()
# bricks = bricks[::-1]
# print(bricks)

for i in range(height):
    # place a row of bricks
    widthLeft = width
    # print(i)

    while widthLeft > 0:
        # print(bricks)
        # takes a brick out of the pile
        brick = bricks.pop(0)
        # print(brick)
        # print(widthLeft)
        # can he place it?
        if(brick <= widthLeft):
            # places it
            widthLeft = widthLeft - brick
        else:
            print('NO')
            exit()
        # if(len(bricks) == 0 and not i == height-1 and not widthLeft == 0):

            # this solves a harder problem
            # found = False
            # find the biggest brick that fits in the row
            # for brick in bricks:
            #     print("width left: " + str(widthLeft))
            #     # print(brick)
            #     # print(widthLeft)
            #     if(brick <= widthLeft):
            #         # place it
            #         widthLeft = widthLeft - brick
            #         bricks.remove(brick)
            #         print(bricks)
            #         # keep going until the row is filled
            #         found = True

print("YES")
