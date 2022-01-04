if __name__=="__main__":
    n = int(input())
    arr = [0] * (n + 2)
    arr[1], arr[2] = 1, 3

    for i in range(3, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]*2

    # print(arr)
    print(arr[n] % 10007)