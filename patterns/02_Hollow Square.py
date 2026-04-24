def pattern(n):
    for i in range(n, 0, -1):
        if i==n or i==1:
            for j in range(1, n+1, +1):
                print("*", end=" ");
            print();
        else:
            for k in range(1, 2, +1):
                print("*", end=" ");
            for l in range(1, n-1, +1):
                print("", end="  ");
            for m in range(1, 2, +1):
                print("*", end=" ");
            print()
n=int(input("please enter your numbers:"))
pattern(n);