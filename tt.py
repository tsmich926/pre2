T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    mx = 0 #N*M최댓값
    #3개의 영역으로 나누기
    for i in range(N-2):
        for j in range(i+1,N-1):
            cnt = 0
            for k in range(i+1):
                cnt += arr[k].count('W')
            for k in range(i+1,j+1):
                cnt += arr[k].count('B')
            for k in range(j+1,N):
                cnt += arr[k].count('R')
            mx = max(mx,cnt)
    print(f'#{tc} {N*M-mx}')