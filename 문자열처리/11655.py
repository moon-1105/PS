if __name__ =="__main__":
    word = input()
    answer = ""
    for ch in word:
        if ch.isalpha():
            tmp = ord(ch) + 13
            if ch.isupper():
                if tmp > 90:
                    tmp = tmp-90+65-1
            else:
                if tmp > 122:
                    tmp = tmp-122+97-1
            answer += chr(tmp)
        else:
            answer += ch
    print(answer)