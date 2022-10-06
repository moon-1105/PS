if __name__ =="__main__":
    N, K = input().split()
    N, K = int(N),int(K)
    people = []
    for idx in range(1,N+1):
        people.append(idx)
    print(people)
    idx = K
    answer= []
    pos = 0
    while(len(answer)!=N):
        if idx >= N:
            idx=idx-N
        print(idx, end=" => ")
        if idx not in answer:
            answer.append(idx)
            idx += K
        else:
            idx += 1
    print(answer)
