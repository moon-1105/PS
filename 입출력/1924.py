if __name__=="__main__":
    x, y = map(int, input().split())
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = 0
    for i in range(0, x-1):
        days+=months[i]
    days += y
    #print(days)
    week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    print(week[days%7])