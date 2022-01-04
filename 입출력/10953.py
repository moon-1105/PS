if __name__=="__main__":
    N = int(input())
    for _ in range(0,N):
        A, B = map(int, input().split(","))
        print(A+B)