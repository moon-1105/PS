if __name__=="__main__":
    N = int(input())
    wines = []
    for _ in range(N):
        wines.append(int(input()))
    arr = [0]*(N+1)
    if len(wines) < 3:
        print(sum(wines))
        exit(0)
    arr[0] = wines[0]
    arr[1] = wines[0]+wines[1]
    arr[2] = max(wines[0]+wines[2], wines[1]+wines[2], arr[1])

    for i in range(3, N):
        arr[i] = max(arr[i-1], wines[i]+arr[i-2], wines[i]+wines[i-1]+arr[i-3])

    """
    wines[i]+wines[i-1]+arr[i-3]
    => arr[i-2]를 확실하게 배제하기 위해서 
    """
    print(max(arr))
    #경우의수 골고루 생각해서 다시 하기