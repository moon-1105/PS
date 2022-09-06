import math
if __name__ =="__main__":
    N = int(input())
    arr = [0]*(N+1)
    arr[0] = 1
    arr[2] = 3
    for i in range(4, N+1):
        arr[i] = arr[i-2]*3+2
    print(arr[N])