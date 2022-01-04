if __name__=="__main__":
    sentence = input()
    res = ""
    for ch in sentence:
        res += ch
        if len(res) >= 10 :
            print(res)
            res = ""
    print(res,end="")