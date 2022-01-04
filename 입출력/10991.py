if __name__=="__main__":
    N = int(input())
    for i in range(0,N):
        res = ""
        for j in range(0, N-i-1):
            res+=" "
        for j in range(0,i+1):
            res+="* "
        print(res[:-1])

