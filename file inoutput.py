# 파일입출력

# 첫번째 실습
score_file = open("score.txt", "w", encoding="utf8") # open("파일이름", "w", encoding="utf8"), "w"는 write로 이 파일은 쓰기 위한 목적으로 열겠다, encoding="utf8"을 정의해줘야 한글 출력을 위해
print("수학: 0", file=score_file)
print("영어: 50", file=score_file)
score_file.close()

# 두번째 실습
score_file = open("score.txt", "a", encoding="utf8") # "w"로 쓰면 덮어쓰기가 되니깐 이미 있는 파일에 이어서 작성하고자 하면 append를 의미하는 "a"로 씀
score_file.write("과학: 80")
score_file.write("\n코딩: 100")
score_file.close()


# 세번째 실습
score__file = open("score.txt", "r", encoding="utf8") # "r"은 read로 파일을 읽어오는 용도로 파일을 열겠다

한번에 다 읽는거
print(score__file.read())
score__file.close()
# 결과: 
# 수학: 0  
# 영어: 50 
# 과학: 80 
# 코딩: 100

# 한 줄 한 줄 불러와서 처리
score__file = open("score.txt", "r", encoding="utf8")
print(score__file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score__file.readline())
print(score__file.readline())
print(score__file.readline())
score__file.close()
# 결과: 
# 수학: 0

# 영어: 50

# 과학: 80

# 코딩: 100

# 한 줄 한 줄 불러와서 처리하는 줄바꿈 없이 할 때
score__file = open("score.txt", "r", encoding="utf8")
print(score__file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score__file.readline(), end="")
print(score__file.readline(), end="")
print(score__file.readline(), end="")
score__file.close()

# 결과:
# 수학: 0
# 영어: 50
# 과학: 80
# 코딩: 100

# 몇 줄인지 모를 때
score__file = open("score.txt", "r", encoding="utf8")
while True: # 무한루프, 계속 반복문 수행
    line = score__file.readline()
    if not line: # 읽어온 내용이 없으면
        break
    print(line) # 라인에 내용이 있으면 읽어오기
score__file.close()

# 몇 줄인지 모르고 줄바꿈 안하고 싶을 때
score__file = open("score.txt", "r", encoding="utf8")
while True: # 무한루프, 계속 반복문 수행
    line = score__file.readline()
    if not line: # 읽어온 내용이 없으면
        break
    print(line, end="") # 라인에 내용이 있으면 읽어오기
score__file.close()

# 리스트에 값을 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="") # score_file의 모든 줄을 가져와서 list 형태로 집어넣고 리스트에서 한 줄씩 불러와서 출력해주는 형태 

score_file.close()