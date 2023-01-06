from queue import PriorityQueue

if __name__=="__main__":
    N = int(input())
    que = PriorityQueue()
    for _ in range(N):
        que.put(int(input()))

    while not que.empty() :
        val = que.get()
        print(val)
