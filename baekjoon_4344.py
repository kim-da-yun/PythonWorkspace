c = int(input()) # 테스트 케이스의 개수를 입력 받음

for i in range(c): # c번 반복함
    scores = list(map(int, input().split()))
    avg = sum(scores[1:]) / scores[0] # 1번째 요소부터 마지막 요소까지 더한 후 학생의 수(scores[0])로 나눠준 뒤 저장함

    cnt = 0
    
    for i in scores[1:]: # 1번째 요소부터 평균이 넘는지 확인
        if i > avg: # 평균을 넘으면
            cnt += 1 # 카운트에 1을 더해줌

    percent = (cnt/scores[0]) * 100 # cnt를 학생의 수로 나눠준 다음 100을 곱해줌
    print('%.3f' %percent + '%') # 소수점 셋째 자리까지 출력함
