#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 시각화 도구
# Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# 폰트 추가
from matplotlib import font_manager, rc
font_path = "./malgun.ttf" # 폰트파일의 위치
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)

df = pd.read_excel('시도별 전출입 인구수.xlsx', header = 0) # 내용이 없는 부분을 0으로 채워서 처리해라, 헤더를 0으로 처리


# In[2]:


print(df)


# In[3]:


df = df.fillna(method = 'ffill')


# In[4]:


print(df)


# In[5]:


mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
# 서울에서 서울이 아닌 지역으로 갔을 때

# mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] == '서울특별시') 
# 서울에서 서울로 옮겼을 때


# In[6]:


df_seoul = df[mask] # 조건문을 df에 적용해서 조건을 만족하는 행만 추출
print(df_seoul)


# In[7]:


df_seoul = df_seoul.drop(['전출지별'], axis = 1) 
# 열 기준으로 삭제
df_seoul.rename({'전입지별' : '전입지'}, axis =1, inplace = True)  
# 이름 변경, 전입지별을 전입지로 변경


# In[8]:


df_seoul.set_index('전입지', inplace = True) 
# 전입지라는 열을 새로운 인덱스로 하겠음


# In[9]:


print(df_seoul)


# In[10]:


s = df_seoul.loc['경기도']


# In[11]:


print(s)


# In[12]:


plt.plot(s.index, s.values)
# 경기도 관련된 데이터 첫번째를 인덱스로 사용(s.index: x축), 
# s.values(y축)를 통해 이동한 인원 수가 나옴


# In[13]:


plt.plot(s)


# In[14]:


plt.figure(figsize = (14, 5))
plt.xticks(rotation='vertical')
plt.plot(s.index, s.values)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'], loc = 'best') # 범례
plt.show() # 그래프를 다시 그리기


# In[16]:


plt.style.use('ggplot') # 스타일 적용 - > 
# 보기 좋은 형태 그래프로 만듦, ggplot: 회색, grid가 들어가있음
plt.figure(figsize = (14, 5))
plt.xticks(rotation='vertical') # x레벨 레이블을 세로로 돌림
plt.plot(s.index, s.values)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'], loc = 'best') # 범례
plt.show() # 그래프를 다시 그리기


# In[17]:


# 스타일 목록
print(plt.style.available)


# In[18]:


plt.style.use('dark_background') 
plt.figure(figsize = (14, 5))
plt.xticks(rotation='vertical')
plt.plot(s.index, s.values)
plt.title('서울 -> 경기 인구 이동')
plt.xlabel('기간')
plt.ylabel('이동 인구수')
plt.legend(labels=['서울 -> 경기'], loc = 'best') # 범례
plt.show() # 그래프를 다시 그리기


# In[19]:


# 상승하는 쪽과 감소하는 쪽에 대해 추가 설명을 할 때 화살표 생성
fig = plt.figure(figsize = (10, 10))
ax1 = fig.add_subplot(2, 1, 1) # (2, 1)
ax2 = fig.add_subplot(2, 1, 2) 

ax1.set_xticklabels(s.index, rotation='vertical') 
ax1.plot(s.index, s.values, marker = 'o', markersize = 10) 
# 각각 연도별 위치 부각

ax2.set_xticklabels(s.index, rotation='vertical') 
ax2.plot(s.index, s.values, marker = 'o', markersize = 10)

# plt.title('서울 -> 경기 인구 이동')
# plt.xlabel('기간')
# plt.ylabel('이동 인구수')
# plt.legend(labels=['서울 -> 경기'], loc = 'best') # 범례
# plt.ylim(5000, 800000) # y축 한계값
# # 내려가는 화살표
# plt.annotate('', # 화살표가 어디에서 시작해서 어디로 가냐
#              xy = (47, 450000),     # 화살표의 머리 부분(끝점)
#              xytext = (30, 580000), # 화살표의 꼬리 부분(시작점)
#              xycoords = 'data',     # 좌표 체계
#              arrowprops = dict(arrowstyle = '->', color = 'olive', lw = 5), 
                # 화살표 서식
#             )
# # 올라가는 화살표
# plt.annotate('', 
#              xy = (20, 620000),     # 화살표의 머리 부분(끝점)
#              xytext = (2, 290000), # 화살표의 꼬리 부분(시작점)
#              xycoords = 'data',     # 좌표 체계
#              arrowprops = dict(arrowstyle = '->', color = 'skyblue', lw = 5), 
                # 화살표 서식
#             )

# plt.annotate('인구이동 증가(1970-1995)', # 텍스트 입력
#               xy = (10, 425000),         # 텍스트 위치 기준점 
#               rotation = 25,             # 텍스트 회전각도
#               va = 'baseline',           # 텍스트 상하 정렬
#               ha = 'center',             # 텍스트 좌우 정렬
#               fontsize = 15,             # 텍스트 크기
#               )
             
plt.show() 


# In[20]:


# 전출지 = 서울, 전입지 = 경기도, 충청남도, 강원도
s = df_seoul.loc[['경기도', '충청남도', '강원도']]


# In[21]:


print(s)


# In[24]:


fig = plt.figure(figsize = (20, 5))
ax1 = fig.add_subplot(1, 1, 1)

# ax1.set_xticklabels(s.index, rotation='vertical')
# x축의 레이블은 x 자체가 데이터프레임 형태라 인덱스 사용 안하기 때문에 삭제
ax1.plot(s.loc['경기도',:], marker = 'o', markersize = 10, label = '서울 -> 경기') 
# s에 결과를 저장 / 시리즈가 아닌 
# 데이터프레임이라 인덱스와 value 구분 안해도 됨 
# -> 경기도의 전체 행을 가져오면 경기도의 모든 행의 데이터가 시리즈로 변환됨
# :은 행 전체(처음부터 끝까지)
ax1.plot(s.loc['충청남도',:], marker = 'o', markersize = 10, label = '서울 -> 충남')
ax1.plot(s.loc['강원도',:], marker = 'o', markersize = 10, label = '서울 -> 강원')

ax1.legend(loc = 'best') # 레전드의 위치 조정

plt.show()

rc('font', family = font_name) # 폰트


# In[30]:


# subplot을 이용하면 x에서 갖고있는 데이터가 각각의 지역별 이동 현황을 담고 있어 보여주고 싶은 지역별로 한 화면 내에 정리된 그래프로
# 내용들을 보여줄 수 있음

# 4지역으로의 이동을 전체 그래프를 4개로 나눠서 보여주는 처리
s2 = df_seoul.loc[['경기도', '충청남도', '강원도', '경상북도']] # 4개의 지역으로 이동한 데이터를 가져옴
fig = plt.figure(figsize = (20, 10)) # 20 * 10 size
ax1 = fig.add_subplot(2, 2, 1) # subplot은 총 4개를 저장해야되니 2*2 영역으로
ax2 = fig.add_subplot(2 ,2, 2)
ax3 = fig.add_subplot(2 ,2, 3)
ax4 = fig.add_subplot(2 ,2, 4)

ax1.plot(s2.loc['경기도',:], marker = 'o', markersize = 10, color = 'olive', linewidth = 2, label = '서울 -> 경기') 
# linewidth: 라인에 대한 폭 조정
ax2.plot(s2.loc['충청남도',:], marker = 'o', markersize = 10, color = 'blue', linewidth = 2, label = '서울 -> 충남')
ax3.plot(s2.loc['강원도',:], marker = 'o', markersize = 10, color = 'magenta', linewidth = 2, label = '서울 -> 강원')
ax4.plot(s2.loc['경상북도',:], marker = 'o', markersize = 10, color = 'yellow', linewidth = 2, label = '서울 -> 경북')

ax1.set_title('서울 -> 경기', size = 15)
ax2.set_title('서울 -> 충남', size = 15)
ax3.set_title('서울 -> 강원', size = 15)
ax4.set_title('서울 -> 경북', size = 15)

# x축에 대한 레이블 회전
ax1.set_xticklabels(s2.columns, rotation = 90)
ax2.set_xticklabels(s2.columns, rotation = 90)
ax3.set_xticklabels(s2.columns, rotation = 90)
ax4.set_xticklabels(s2.columns, rotation = 90)

plt.show()


# In[33]:


# 면적 그래프
# plot 옵션에서 kind를 수정하면 됨
# 면적그래프는 transpose해서 가로, 세로를 바꿈
s3 = df_seoul.loc[['경기도', '충청남도', '강원도', '경상북도']] 
s3 = s3.transpose() # 가로, 세로 바뀐 형태로 저장됨 / 연도: 인덱스 
s3.index = s3.index.map(int)# 연도를 정수형으로 변경
s3.plot(kind = 'area', stacked = False, alpha = 0.2, figsize = (20, 10)) 
# alpth = 0.2(0~1사이 지정) : 면적이 4개의 지역에 대한 각각이 한 그래프에 겹쳐지니 투명하게 설정
plt.legend(loc = 'best', fontsize = 15) # 색 구분
plt.show()


# In[35]:


s3 = df_seoul.loc[['전라남도', '충청남도', '강원도', '경상북도']] 
s3 = s3.transpose() # 가로, 세로 바뀐 형태로 저장됨 / 연도: 인덱스 
s3.index = s3.index.map(int)# 연도를 정수형으로 변경
s3.plot(kind = 'area', stacked = True, alpha = 0.2, figsize = (20, 10)) 
plt.legend(loc = 'best', fontsize = 15) # 색 구분
plt.show()


# In[36]:


# 막대그래프
s3 = df_seoul.loc[['전라남도', '충청남도', '강원도', '경상북도']] 
s3 = s3.transpose() # 가로, 세로 바뀐 형태로 저장됨 / 연도: 인덱스 
s3.index = s3.index.map(int)# 연도를 정수형으로 변경
s3.plot(kind = 'bar', figsize = (20, 10), width = 0.7, color = ['orange', 'green', 'blue', 'yellow'] ) # 막대 사이의 폭 크기 지정
plt.legend(loc = 'best', fontsize = 15) # 색 구분
plt.show()


# In[38]:


# 가로 방향, horizontal 막대그래프
s4 = df_seoul.loc[['전라남도', '충청남도', '강원도', '경상북도']] 
# 마지막 colunmn에 연도별 합계를 추가
s4['합계'] = s4.sum(axis = 1) # 한 행당 이동인구가 전체 연도에 걸쳐서 합산되어 저장됨. 가로 방향으로 지정.
s4['합계'].plot(kind = 'barh', figsize = (10, 5), width = 0.7, color = ['orange', 'green', 'blue', 'yellow'])
plt.show()


# In[41]:


# 가로 방향, horizontal 막대그래프
s4 = df_seoul.loc[['전라남도', '충청남도', '강원도', '경상북도']] 
# 마지막 colunmn에 연도별 합계를 추가
s4['합계'] = s4.sum(axis = 1) # 한 행당 이동인구가 전체 연도에 걸쳐서 합산되어 저장됨. 가로 방향으로 지정.
# 오름차순 정렬
d5 = s4[['합계']].sort_values(by = '합계', ascending = False) # ascending은 정렬의 증가하는 방향을 설정, 큰 -> 작은: False
d5.plot(kind = 'barh', figsize = (10, 5), width = 0.7, color = ['orange', 'green', 'blue', 'yellow'])
plt.show()


# In[ ]:




