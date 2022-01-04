if __name__=="__main__":
    N = int(input())
    print(" "*(N-1) + "*")

    for i in range(1,N-1):
        res = ""
        for j in range(0, N-i-1):
            res+=" "
        res+="*"
        for j in range(0, 2*i-1):
            res+=" "
        res += "*"
        print(res)
    if N >=2:
        print("*"*(2*N-1))