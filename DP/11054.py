"""
수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이
1. 해당 수를 포함했을 때의 바이토닉 수열 길이
2. 안포함했을때 바이토닉 길이 => 비교

"""

if __name__=="__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    if N == 1:
        # 여기서 프린트 첫번째 인풋 한거 실환가
        print(1)
        exit(0)

    arr = [0] * (N + 1)
    arr[0] = [nums[0]]


    print(ans)