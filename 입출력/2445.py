if __name__ =="__main__":
    N = int(input())
    for i in range(1, N):
        for j in range(0, i):
            print("*", end="")
        for j in range(0, 2*(N-i)):
            print(" ", end="")
        for j in range(0, i):
            print("*", end="")
        print()
    print("*"*N*2)
    for i in range(1, N):
        for j in range(0, N-i):
            print("*", end="")
        for j in range(0, 2*i):
            print(" ", end="")
        for j in range(0, N-i):
            print("*", end="")
        print()