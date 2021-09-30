# pickle

import pickle

profile_file = open("profile.pickle", "wb") # 쓰기 목적으로 w / b는 binary로 pickle을 쓰기 위해서는 binary 타입을 정의해줘야 함 / pickle은 따로 인코딩을 지정해줄 필요 없음
profile = {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
print(profile)
# pickle을 이용해서 이 데이터를 파일에 쓰는 게 중요
pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()