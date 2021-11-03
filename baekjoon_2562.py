a = [] # 빈 리스트 생성
for i in range(9): 
    a.append(int(input())) # append를 9번 반복하여 a 리스트에 입력한 9개를 저장함
print(max(a))
print(a.index(max(a)) + 1) # index 값은 0을 포함하지만, a 리스트에는 존재하지 않으므로 값 오류가 발생해 index로 출력한 위치에 1을 더해줘야 올바른 위치를 출력함