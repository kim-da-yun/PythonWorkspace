T = int(input()) # T에 테스트 케이스의 개수를 입력받음
for x in range(1, T+1):
    A, B = map(int, input().split()) # 공백을 사이에 두고 한 줄로 입력 받음
    print(f'Case #{x}: {A} + {B} = {A+B}') # f-string을 이용해 {}를 이용해 변수를 입력함.  f를 붙이고 변수를 넣을 위치에 {변수} 형태로 사용
