if __name__=="__main__":
    N = int(input())
    for i in range(0,N):
        A, B = map(int, input().split())
        res = "Case #"+str(i+1)+": "+str(A+B)
        print(res)