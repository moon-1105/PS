if __name__=="__main__":
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    arr.sort()

    for ele in arr:
        print(ele)
