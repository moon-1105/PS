import sys
if __name__ =="__main__":
    arr = []
    while 1 :
        try:
            string = input()
            #print(string)
            if string == "":
                break;

            answer = [0] * 4
            for ch in string:
                if ch.isalpha():
                    if ch.islower():
                        answer[0] = answer[0]+1
                    else:
                        answer[1] =answer[1]+ 1
                if ch.isdigit():
                    answer[2] += 1
                if ch == ' ':
                    answer[3] += 1
            for ch in answer :
                print(ch, end=" ")
            print()
        except EOFError:
            break

