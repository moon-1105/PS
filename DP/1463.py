"""
숫자 i 를 만드는 방법이 여러개라 혼란했는데
i를 직접 만드는게 아니라
arr[i] 는 i 로 가는 방법의 수
"""

if __name__=="__main__":
    N = int(input())
    arr=[0]*(N+10)
    if N == 1:
        print(0)
        exit(0)
    if N <= 3:
        print(1)
        exit(0)
    arr[1], arr[2], arr[3] = 0, 1, 1
    for i in range(4, N+1):
        if i % 6 ==0 :
            arr[i] = min(arr[i//3], arr[i//2], arr[i-1])+1
        elif i % 3 ==0 :
            arr[i] = min(arr[i // 3], arr[i - 1])+1
        elif i % 2 ==0 :
            arr[i] = min(arr[i // 2], arr[i - 1])+1
        else:
            arr[i] = arr[i-1]+1
    #print(arr)
    print(arr[N])


