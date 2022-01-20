"""
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열

"""
def findSmall(n, nums, arr):
    mVal = -1
    for i in range(0, n):
        if nums[i] < nums[n]:
            mVal = max(mVal, arr[i])
    return mVal

if __name__=="__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    if N == 1:
        print(1)
        exit(0)
    arr = [0]*(N+1)
    arr[0] = 1
    if nums[0] < nums[1]:
        arr[1] = 2
    else:
        arr[1] = 1

    for i in range(2, N):
        #print(arr)
        val = findSmall(i, nums, arr)
        if val == -1 :
            arr[i] = 1
        else:
            arr[i] = val+1
    #여기를 무조건 마지막 수를 포함하는 걸로 했음..
    print(max(arr))