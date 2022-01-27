"""
수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이
1. 바이토닉 수열을 아예 구하고
2. 그 길이를 비교
"""
def plus(arr, value):
    tmp = arr.copy()
    tmp.append(value)
    return tmp

if __name__=="__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    if N == 1:
        # 여기서 프린트 첫번째 인풋 한거 실환가
        print(1)
        exit(0)

    arr = [0] * (N + 1)
    arr[0] = [nums[0]]

    if nums[0] > nums[1]:
        arr[1] = plus(arr[0], nums[1])
    else:
        arr[1] = [nums[1]]

    for i in range(2, N):
        # print("#", i, arr)
        MaxArr = []
        for j in range(0, i):
            # 바이토닉이 맞는지는 판단하기.. 모든 수열 다 구해야하나?
            # 이전거보다 크거나
            # 젤 큰거보다 작거나
            if min(arr[j]) > nums[i]:
                # 길이가 긴지
                if len(arr[j]) > len(MaxArr):
                    MaxArr = arr[j].copy()
                elif len(arr[j]) == len(MaxArr):
                    if min(arr[j]) > min(MaxArr):
                        MaxArr = arr[j].copy()

        arr[i] = plus(MaxArr, nums[i])

    ans = 0
    for i in range(0, N):
        ans = max(len(arr[i]), ans)
    print(ans)