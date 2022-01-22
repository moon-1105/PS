"""
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열
1. 감소수열을 아예 구하고
2. 길이를 비교
"""
def plus(arr, value):
    tmp = arr.copy()
    tmp.append(value)
    return tmp

if __name__=="__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    if N == 1:
        print(nums[0])
        exit(0)

    arr = [0]*(N+1)
    arr[0] = [nums[0]]

    if nums[0] > nums[1]:
        arr[1] = plus(arr[0],nums[1])
    else:
        arr[1] = [nums[1]]

    for i in range(2, N):
        #print("#", i, arr)
        MaxArr = []
        for j in range(0, i):
            #증가수열이 맞는지
            if min(arr[j]) > nums[i]:
                #길이가 긴지
                if len(arr[j]) > len(MaxArr):
                    MaxArr = arr[j].copy()
                elif len(arr[j]) == len(MaxArr):
                    if min(arr[j]) > min(MaxArr):
                        MaxArr = arr[j].copy()

        arr[i] = plus(MaxArr, nums[i])

    #여기를 무조건 마지막 수를 포함하는 걸로 했음..
    #print(arr)
    ans = 0
    for i in range(0,N):
        ans = max(len(arr[i]), ans)
    print(ans)