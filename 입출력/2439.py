if __name__ =="__main__":
    N = int(input())
    for i in range(1, N+1):
        for j in range(0,N-i):
            print(" ",end="")
        for j in range(0, i):
            print("*", end="")
        print()
