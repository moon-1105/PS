if __name__ =="__main__":
    N, K = input().split()
    N, K = int(N),int(K)

    people = []
    for idx in range(1,N+1):
        people.append(idx)
    print(people)
    idx = K
    answer= []
    while(len(answer)!=N and len(people)!=0):
        if idx > len(people):
            idx = idx-len(people)
        print(idx)
        #while(people[idx-1] in answer):
        #    idx+=1
        answer.append(people.pop(idx-1))
        print(answer)
        idx+=K
