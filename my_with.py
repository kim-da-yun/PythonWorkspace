# with

import pickle

with open("profile.pickle", "rb") as profile_file: # 파일("profile.pickle)을 열어서 profile_file이라는 변수로 저장해두고 파일 내용을 pickle.load를 통해서 불러와서 출력을 해줌
    print(pickle.load(profile_file)) # 따로 열었던 파일을 close 할 필요없이 with문을 탈출하면서 자동으로 종료해줌

# pickle 사용하지 않고 일반적인 파일을 쓰고읽는걸 with로 활용해보려 함
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파일썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())    