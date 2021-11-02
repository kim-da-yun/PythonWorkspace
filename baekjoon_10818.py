a = int(input())
b = list(map(int, input().split()))

print(min(b), max(b))

# 또 다른  방법

a = int(input())
b = list(map(int, input().split()))

max = b[0] # max 값을 저장할 변수에 리스트의 첫 번째 값을 저장함
min = b[0] 

for i in b[1:]:
    if i > max: # 두 번째 값부터 마지막 값까지 차례로 비교함
        max = i # 비교하면서 max보다 크면 값을 바꿈
    elif i < min:
        min = i

print(min, max)