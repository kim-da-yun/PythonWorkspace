year = int(input()) # 연도 입력 받기

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0: # 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때
    print('1') # 윤년이면 1 출력

else:
    print('0') # 아니면 0 출력

