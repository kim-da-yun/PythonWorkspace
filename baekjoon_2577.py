A = int(input())
B = int(input())
C = int(input())

num = list(str(A * B *C)) # 계산 값을 문자열로 변환 후 리스트로 저장

for i in range(10): # 문자열로 변환, 0 ~ 9
    print(num.count(str(i))) 
