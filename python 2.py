






for i in range(1, 7):
    for j in range(1, 7):
        if i == 1 or i == 6 or j == i or j == 7 - i:
            print("*", end="")
        else:
            print(" ", end="")
    print()