if __name__ =="__main__":
    N = int(input())
    for i in range(1, N):
        for j in range(1, i):
            print(" ", end="")
        for j in range(0, 2*(N-i)+1):
            print("*", end="")
        print()
    print(" "*(N-1)+"*")
    for i in range(1, N):
        for j in range(1, N-i):
            print(" ", end="")
        for j in range(0, 2*i+1):
            print("*", end="")
        print()
