def patter(n):
    for i in range(n+1):
        for j in range(i):
            print("*", end="");
        print();

n=int(input("Please enter your numbers: "));
patter(n);