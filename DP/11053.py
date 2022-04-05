"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열
"""

def findBitonic(n, nums, arr):
    mVal = -1
    return mVal

if __name__=="__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    if N == 1:
        print(1)
        exit(0)
    arr = []
    for _ in N :
        arr.append([0] * (N + 1))
     #첫줄은 포함/ 둘째줄은 안포함
    arr[0][0] = 1
    if nums[0] < nums[1]:
        arr[1][0] = 2
    else:
        arr[1][1] = 1

    for i in range(2, N):
        print(arr)
        val = findBitonic(i, nums, arr)
        if val == -1 :
            arr[i] = 1
        else:
            arr[i] = val+1
    #이중표로 만들어서 해당 수가 포함했을 때 / 안했을때 나눠서 가야할거같은데
    print(max(arr))


