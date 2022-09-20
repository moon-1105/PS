
if __name__ =="__main__":
    word = input()
    answer = []
    for ch in word:
        answer.append(ch)
    N = int(input())
    cmd = []
    for _ in range(N):
        cmd.append(input())
    idx = len(word)-1
    for c in cmd :
        if c[0] == 'P':
            if idx!=0 :
                answer.insert(idx+1,c[2])
            else:
                answer.insert(0, c[2])
            idx+=1
        elif c[0] == 'L':
            if idx!=0:
                idx-=1
        elif c[0] == 'D':
            if idx!=len(answer)-1:
                idx +=1
        elif c[0] == 'B':
            if idx!=0:
                answer.pop(idx-1)
            idx-=1
        #print(idx, answer)
        ans = ""
    for ch in answer:
        ans += ch
    print(ans)

