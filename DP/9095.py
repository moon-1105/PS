if __name__=="__main__":
    T = int(input())
    for _ in range(0,T):
        n = int(input())
        #정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수
        arr = [0]*(n+3)
        arr[1], arr[2], arr[3] = 1, 2, 4
        for i in range(4, n+1):
            arr[i] = arr[i-3]+arr[i-2]+arr[i-1]
        print(arr[n])
