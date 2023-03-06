T= int(input())
for tc in range(1,T+1):
    N,M = int(input().split())
    arr = [input() for _ in range(N)]
    mmin = 999
    for i in range(0,N-2):
        for j in range(i+1,N-1):
            for k in range(j+1,N):
                a = arr[i].count('W')
                b = arr[j].count('B')
                c=arr[k].count('R')
                mmin = min((N*M)-(a+b+c) ,mmin)
    print(mmin)