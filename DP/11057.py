if __name__=="__main__":
    N = int(input())
    num = [[0]*10 for _ in range(0,N+1)]
    print(num)
    """
      시작하는 수 #수는 0으로 시작할 수 있다.
      0  1  2  3  4 .... 8  9
    1 1  1  1  1  1 .....1  1
    2 10  9  8  7  6 .....2  1 
    3 55 
       
    """
    num[1] = [1,1,1,1,1,1,1,1,1,1]
    num[2] = [10,9,8,7,6,5,4,3,2,1]
    print(sum(num[1]))
    print(sum(num[2]))
    for i in range(2, N+1):
        for j in range(1, 10):
            num[i][0] = sum(num[i-1])
            num[i][j] = num[i][j-1] - num[i-1][j]
    print(num)
    print(sum(num[N]))