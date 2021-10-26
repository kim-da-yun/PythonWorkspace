# a, b = map(int, input().split())
# print(a+b)



# # 설명
# a = input().split() # a에 1,2를 할당하면 [1, 2]가 할당됨
# b = input() # b에 1,2를 할당하면 1 2가 할당됨

# c, d = input().split()
# print(c+d) # c, d 값에 각각 1, 2를 입력하면 12가 나옴. 형변환이 필요함
# # 형 변환
# c = int(c)
# d = int(d)
# print(c+d)

# # map 함수 / e, f에 할당받는 값을 자동으로 int로 형변환 됨
# e, f = map(int, input().split())
# print(e + f) 

# e, f = map(int, input().split(',')) # ,로 구분하여 입력 받기 예) 1, 2 -> 3
# print(e + f) 
