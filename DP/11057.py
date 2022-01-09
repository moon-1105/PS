if __name__=="__main__":
    N = int(input())
    num = [[0]*10 for _ in range(0,N+1)]
    """
      시작하는 수 #수는 0으로 시작할 수 있다.
      0  1  2  3  4 .... 8  9
    1 1  1  1  1  1 .....1  1
    2 10  9  8  7  6 .....2  1 
    3 55 
       
    """
    num[1] = [1,1,1,1,1,1,1,1,1,1]
    for i in range(2, N+1):
        for j in range(0, 10):
            num[i][j] = sum(num[i - 1][j:])
    #print(num)
    print(sum(num[N])%10007)