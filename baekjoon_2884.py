h, m = map(int,input().split())

if m >= 45:
    print(h, m-45) # 45분 이상이면 m-45한 값을 출력

elif m < 45 and h>0:
    print(h-1, m+15) # 45분 미만이면 h-1을 해주고 m+15한 값을 출력

else:
    print(23, m+15) # 00시이면 23시간으로 출력