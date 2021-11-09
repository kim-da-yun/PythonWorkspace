x = int(input())
y = int(input())

if x > 0 and y > 0: # x, y 둘 다 양수면 제 1사분면
    print("1")

elif x < 0 and y > 0: # x가 음수, y가 양수면 제 2사분면
    print("2")

elif x < 0 and y < 0: # x, y 둘 다 음수면 제 3사분면
    print("3")

else:
    print("4") # 위에 다 속하지 않는 x가 양수, y가 음수면 제 4사분면