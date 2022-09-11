if __name__ =="__main__":
    S = input()
    chars = [0]*26
    for i in range(0,26):
        if S.find(chr(i+97)) != -1:
            chars[i] = S.find(chr(i+97))
        else:
            chars[i] = -1

    for ele in chars:
        print(ele, end=" ")
