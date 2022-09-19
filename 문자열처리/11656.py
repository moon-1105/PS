if __name__ =="__main__":
    word = input()
    #make_footage
    arr = []
    for i in range(0, len(word)):
        arr.append(word[-i:])
    arr.sort()
    for ele in arr:
        print(ele)