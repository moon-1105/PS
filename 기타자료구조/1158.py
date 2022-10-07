if __name__ =="__main__":
    N, K = input().split()
    N, K = int(N),int(K)
    people = []
    for idx in range(0,N):
        people.append(idx+1)
    answer= []
    pos, mov = 0, 1
    flag = 0
    while(len(answer)!=N):
        if pos >= N:
            pos = 0
        if mov == K and people[pos] not in answer:
            #print(people[pos],"add")
            answer.append(people[pos])
            #print(answer)
            mov = 1
        if people[pos] not in answer:
            mov+=1
        pos+=1

    print(answer)
    #<3, 6, 2, 7, 5, 1, 4>