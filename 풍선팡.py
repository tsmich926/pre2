T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    mmax = 0
    for row in range(N):
        for col in range(M):
            ssum = arr[row][col]
            for i in range(4):
                newr=row+dr[i]
                newc=col+dc[i]
                if 0<=newr<N and 0<=newc<M:
                    ssum+= arr[newr][newc]
                    mmax = max(mmax,ssum)
    print(f'#{tc} {mmax}')


T= int(input())
for tc in range(1,T+1):
    N,M= map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #상하좌우
    mmax = 0
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    for row in range(N):
        for col in range(M):
            sump = arr[row][col]
            for i in range(4):
                newr = row+dr[i]
                newc =col+dc[i]
                if 0<= newr<N and 0<= newc<M:
                    sump+= arr[newr][newc]
            mmax = max(mmax,sump)
    print(f'#{tc} {mmax}')