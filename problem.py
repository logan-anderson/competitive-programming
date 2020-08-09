while True:
    try:
        if "problem" in input().lower():
            print("yes")
        else:
            print("no")
    except EOFError:
        exit()