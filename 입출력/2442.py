if __name__ =="__main__":
    N = int(input())
    for i in range(1, N+1):
        for j in range(1, N-i+1):
            print(" ", end="")
        for j in range(0,2*i-1):
            print("*",end="")
        print()