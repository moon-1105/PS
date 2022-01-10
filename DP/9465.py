# 상냥이가 뗄 수 있는 스티커의 점수의 최댓값
# 스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 모두 찢어져서 사용할 수 없게 된다
if __name__=="__main__":
    T = int(input())
    for _ in range(0,T):
        n = int(input())
        stickers, arr = [], []
        for _ in range(0,2):
            stickers.append(list(map(int, input().split())))
            arr.append([0]*(n+1))
        arr[0][0], arr[1][0] = stickers[0][0], stickers[1][0]

        for j in range(1, n):
            for i in range(0, 2):
                if i==0:
                    arr[i][j] = stickers[i][j] + max(arr[i+1][j-1],arr[i+1][j-2])
                else:
                    arr[i][j] = stickers[i][j] + max(arr[i-1][j-1],arr[i-1][j-2])
        print(max(arr[0][n-1],arr[1][n-1]))
