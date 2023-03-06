# cnt = int(input()) #스위치 수
# Swit = list(map(int,input().split())) #스위치 번호
# N= int(input()) #학생수
# change_lst=[]
# for i in range(N):
#     S,num = map(int,input().split())
#     if S == 1: #학생이 남자인 경우
#         while cnt>mul:
#             for i in range(cnt):
#                 mul = num*i
#                 change_lst.append(mul)
#     else: #학생이 여자인 경우


def convert(plc):
    if lst[plc] ==


cnt = int(input()) #스위치 수
Swit = list(map(int,input().split())) #스위치 번호
Swit.insert(0,0)
print(Swit)
N= int(input()) #학생수
for i in range(N):
    S, num = map(int,input().split())
    if S == 1:  # 학생이 남자인 경우
        for i in range(num, cnt, num):
            if Swit[i] == 1:
                Swit[i] = 0
            else:
                Swit[i] = 1

    else: #학생이 여자인 경우
        ran= min(cnt-num,num-1) #범위를 벗어나지 않도록 해줌
        for i in range(ran): #반복횟수
            if Swit[num-i] == Swit[num+i]:
                if Swit[num-i] ==0:


            else:
                break


