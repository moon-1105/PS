if __name__=="__main__":
    N = int(input())
    wines = []
    for _ in range(N):
        wines.append(int(input()))
    print(wines)
    arr = [0]*(N+1)
    arr[0],arr[1] = wines[0], wines[1]+wines[0]
    """
    arr[i] = arr[i]+arr[i-2] 혹은 arr[i-1]+arr[i-2]
    """
    for i in range(2, N):
        arr[i] = max(arr[i]+arr[i-2], arr[i-1] + arr[i-2])
    print(arr)
    #경우의수 골고루 생각해서 다시 하기