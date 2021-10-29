N, X = map(int, input().split()) # map 함수, int를 이용해서 정수로 값을 입력받음
A = list(map(int, input().split())) # X로 입력되는 값을 int로 list에 넣기 
for i in A:
    if i < X:
        print(i, end=" ")


N, X = map(int, input().split()) # map 함수, int를 이용해서 정수로 값을 입력받음
A = list(map(int, input().split())) # X로 입력되는 값을 int로 list에 넣기 
for i in A:
    if A[i] < X:
        print(A[i], end=" ")