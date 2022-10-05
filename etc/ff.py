def remove_zero(s):
    new_num = ""
    cnt = 0
    for ch in s:
        if ch == '0':
            cnt += 1
        else:
            new_num += ch
    return new_num, cnt


def solution(s):
    answer = []
    num_zero = 0
    #print(str(format(int('4'), 'b')))
    cnt=0
    while s != '1':
        s, cnt = remove_zero(s)
        num_zero += cnt
        #print("0 제거 ",s, num_zero)
        #x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
        s = str(format(len(s), 'b'))
        #print("2진법 ",s)
        cnt+=1
    return [cnt+1, num_zero]

if __name__ =="__main__":
    print(solution("110010101001"))
