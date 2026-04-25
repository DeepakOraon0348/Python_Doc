def pattern(n):
    for i in range(n):
        for j in range(1, n-i, +1):
            print("",end=" ");
        for k in range(i+1):
            print("*", end="");
        print();

pattern(5)