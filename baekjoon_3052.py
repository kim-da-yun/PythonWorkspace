n = []

for i in range(10): # 0 ~ 9까지 반복
    
    a = int(input())
    r = a % 42 # a 값을 42로 나눈 나머지 값
    n.append(r) # n에 추가
    
s = set(n) # 중복 제거
print(len(s)) # 리스트 s의 길이 출력