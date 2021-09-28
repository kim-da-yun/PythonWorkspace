# 표준입출력
# sep=""은 seperate
# print("Python", "Java", sep=" , ", end="?")
# # end="~"": 문장의 끝부분을 ~으로 바꿔달라,연달아 한 문장으로 출력됨 /  기본으로 줄바꿈으로 되어있는데  
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) # 표준출력으로 문장이 찍힘 / 로그처리를 하는데 표준출력에 대해서는 잘 출력되니 신경쓸 필요 없는데
# print("Python", "Java", file=sys.stderr) # 표준에러로 처리됨 / 에러 부분은 확인을해서 코드 수정을 해야되니 따로 처리함

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":") # .ljust(8)은 8칸 공간을 확보한 왼쪽 정렬, rjust는 오른쪽 정렬
    # score은 정수int니깐 str()로 처리해 문자열로 바꿔줌

# 은행 대기순번표
# 001, 002, 003, .....
# zfile()은 0으로 채운다 / () 안에 넣은 숫자만큼의 크기(공간)을 확보를 하고 값을 집어넣는데 값이 없는 공간은 0으로 채워라
# for num in range(1,21):
#     print("대기번호: "+ str(num).zfill(3))

# 표준입력
answer = input("아무 값 입력: ")
print(type(answer)) # 사용자 입력을 통해서 값을 받게 되면 문자열 형태로 저장됨
# print("입력 값은 " + answer + "입니다.")