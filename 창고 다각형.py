N = int(input())
lst = [-1]*1001
mx = mx_idx= 0
for i in range(N):
    L,H = list(map(int,input().split()))
    lst[L] = H
    if mx < H :
        mx_idx, mx = L,H #가장 긴 높이와 인덱스를 저장

#왼쪽부터 mx_idx까지
mmax = 0
nerby = 0
for i in range(mx_idx+1):
    mmax = max(lst[i],mmax)
    nerby += mmax

#오른쪽부터 mx_idx까지
mmax = 0
for j in range(1000, mx_idx,-1):
    mamx = max(lst[j],mmax)
    nerby += mmax

print(nerby)