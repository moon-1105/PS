#N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수
if __name__=="__main__":
    N = int(input())
    arr = [0]*(N+2)
    arr[1],arr[2] =1,1
    for i in range(3, N+1):
        arr[i] = arr[i-1]+arr[i-2]
    print(arr[N])