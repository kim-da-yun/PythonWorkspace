#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv('auto-mpg.csv', header = None)


# In[3]:


df.columns = ['mpg', 'cylinders','displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name' ]


# In[4]:


# 필요한 열 지정
df['mpg'].plot(kind = 'hist', bins = 10, color = 'coral', figsize = (10,5)) # 10개의 구간으로 나눠서 / 가로, 세로의 크기 지정 
# 히스토그램은 연비와 관련된 값이 있는데 특정 구간에서 몇 개의 데이터가 해당되는지 누적해서 보여주는 방식
plt.title('histogram')
plt.xlabel('mpg')
plt.show() # 파이썬에서는 이 코드가 있어야 실행이 됨으로 추가해야 함


# In[5]:


# 산점도 그래프: 두 개의 변수 사이의 관련된 내용이 있는지 2차원 그래프를 통해서 보는 방식 / x, y 값의 수치로 점으로 표현하는 방식
df.plot(kind = 'scatter', x = 'weight', y = 'mpg', c = 'coral', s = 10, figsize = (10,5)) # c: color, s: 점의 크기
plt.show()


# In[6]:


c_size = df.cylinders/df.cylinders.max() * 100 # 실린더 사이즈  /
# 값의 편차가 커서 정규화해서 최대값의 크기에 대한 비율로 계산 / 가장 큰 값을 100으로 지정
df.plot(kind = 'scatter', x = 'weight', y = 'mpg', c = 'coral', s = c_size,alpha = 0.3,  figsize = (10,5)) 
# alpha: 투명도로 겹친 부분을 알 수 있음
plt.savefig('test.png')# 그래프 재사용하거나 파일 형태로 저장
plt.savefig('test2.png', transparent = True)# 투명한 처리를 해서 한 이미지로 저장, 배경이 투명해짐
plt.show()


# In[7]:


df['count'] = 1 # 초기값이 1인 count라는 열 추가
# 해당 origin에 그룹핑 된 결과로 카운트 열에 합산하면 해당 제조국의 물건 갯수 파악할 수 있음
df_origin = df.groupby('origin').sum() # 특정한 열에 들어있는 값을 기준으로 모으는 방법: groupby
print(df_origin)


# In[8]:


df_origin.index = ['USA', 'EU', 'JAPAN'] # 행 인덱스 지정
df_origin['count'].plot(kind = 'pie', figsize = (7,5), autopct = '%1.1f%%',
                       startangle = 10, colors = ['blue', 'yellow', 'red']) # autopct: 출력할 비율 지정
plt.legend(labels = df_origin.index, loc = 'upper right') # 색으로 구분했지만 인덱스 지정한 문자열로 색과 대응되는 legend 지정
plt.show()


# In[9]:


# 한 번에 두 개의 그래프를 그리려면 subplot 형태로 추가하고 작업해야 함
fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1,2,1) # 각각의 subplot이 1*2짜리(하나의 행이 두개의 열로 되어있음)
ax2 = fig.add_subplot(1,2,2) # 2번 영역에 들어갈거

# 박스플롯
ax1.boxplot(x = [df[df['origin'] == 1]['mpg'],
                df[df['origin'] == 2]['mpg'],
                df[df['origin'] == 3]['mpg']], labels = ['USA', 'EU', 'JAPAN']) 
# [df['origin'] == 1]은 논리적인 식을 갖고 어떤 조건을 만족하는 행을 추려내는 구문
# 위 문장은 origin이라는 열의 값이 1번에 해당하는 미국의 데이터를 데이터프레임에서 가져오고 해당 미국 연비에 대한 값을 가져옴
# 위는 왼쪽에 들어갈 그래프임
ax2.boxplot(x = [df[df['origin'] == 1]['mpg'],
                df[df['origin'] == 2]['mpg'],
                df[df['origin'] == 3]['mpg']], labels = ['USA', 'EU', 'JAPAN'],
           vert = False) 
# x에는 3개 항목이 들어가고 레이블이 붙는데 마지막 부분에 vert라는 옵션에 false로 만들어 추가하면 수평 방향으로 박스플롯을 보여줌
# 위는 오른쪽에 들어갈 그래프임
plt.show()
# 박스플롯 이미지의 주황 선은 중간값이 어느쯤에 모여있는지, usa는 중간값이 아래쪽에 모여있음, 평균도 동일


# In[10]:


# 11_2
# Seaborn 라이브러리


# In[11]:


import seaborn as sns

titanic  = sns.load_dataset('titanic')
print(titanic.head())


# In[12]:


# 회귀선이 있는 산점도
sns.set_style('darkgrid') # 스타일 변경


# In[13]:


# 두 개의 그래프를 그리기 위해 화면을 분할
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1) # 1*2가 2개
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='age', y = 'fare', data = titanic, ax = ax1) # regplot: 회귀선 / 타이타닉 데이터프레임에서 fare 열을 가져다 쓰겠다
# ax = ax1은 sns 과정에서 그린 그래프를 어떤 서브플롯에 해야되는지 지정 
sns.regplot(x='age', y = 'fare', data = titanic, ax = ax2) 
# 회귀선 자체를 빼고 그림을 그리고 싶으면 fit_reg=False를 해서 fit_reg 옵션을 flase를 해줘야 함(기본값은 True)


# In[14]:


# 두 개의 그래프를 그리기 위해 화면을 분할
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1) # 1*2가 2개
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x='age', y = 'fare', data = titanic, ax = ax1) # regplot: 회귀선 / 타이타닉 데이터프레임에서 fare 열을 가져다 쓰겠다
# ax = ax1은 sns 과정에서 그린 그래프를 어떤 서브플롯에 해야되는지 지정 
sns.regplot(x='age', y = 'fare', data = titanic, ax = ax2, fit_reg=False) 
# 회귀선 자체를 빼고 그림을 그리고 싶으면 fit_reg=False를 해서 fit_reg 옵션을 flase를 해줘야 함(기본값은 True)


# In[15]:


# 히스토그램 그래프
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1) # 가로로 3개의 영역으로 나눈 다음에 하나씩 들어가게
ax2 = fig.add_subplot(1,3,2)

# 히스토그램은 1개의 열에 대한 데이터를 분석해서 구간 별로 얼마만큼 누적됐는지 보여줌
sns.distplot(titanic['fare'], ax = ax1) # hist 옵션이 기본값 True로 지정된 상태로 그려짐
sns.distplot(titanic['fare'], hist = False, ax = ax2) # 히스토그램에 대한 부분을 false로 하면 히스토그램이 표시가 되지 않는, 
# 면적에 대한 부분을 고려하지 않고 전체적인 히스토그램에서 상단에 남아있는 선만 표현하는 방식으로 해서 그래프 완성
plt.show()


# In[16]:


fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)


sns.distplot(titanic['fare'], ax = ax1) # 매끄럽게 다듬어서 하나의 그래프로 표현
sns.distplot(titanic['fare'], hist = False, ax = ax2) # 아래쪽에 누적되는 아래쪽 면적을 제외하고 위쪽 그래프 부분 확인하기 위해
sns.distplot(titanic['fare'], kde = False, ax = ax3) 
# -> 히스토그램으로 해서 면적에 누적된 내용을 보여주는데 내용을 확률밀도함수 형태(막대그래프 모여있는 형태같은)로 그림
# 전체적으로 스무스하게 라인을 구현되는데 옵션을 커널밀도함수, kde 값을 False로 지정
# 계산값을 빼고 누적된 형태의 히스토그램의 막대그래프 형태로만 표현하겠다.


# In[17]:


# 히트맵

# 범주형 데이터는 연속된 데이터가 아니라 특정한 카테고리 중에 하나가 선택될 수 있는 열을 가리킴
# 특정 범주형 데이터를 가지고 있는 열을 선택을 해서 타이타닉 데이터에서 성별은 여/남 둘 중 하나, 클래스는 3개라서 범주형 데이터임
# 전체 데이터프레임을 성별, 각각의 클래스에 몇명의 사람들이 있었는지 집계를 하는 형태로 테이블을 하나 만들고 
# 해당 테이블을 갖고 각각 교차하는 지점에 얼마만큼의 사람들이 있는지를 컬러로 구분해서 보여주는 방식
table = titanic.pivot_table(index=['sex'], columns = ['class'], aggfunc = 'size') 
# 타이타닉 데이터프레임에서 특정한 피봇 테이블에 가로(index)쪽에 어떤 열을 기준으로 정렬을 할건지, 
# 세로(columns) 쪽 열에 어떤 필드를 사용할지 옵션을 지정
# 피봇시키면서 각각의 행렬이 만나는 지점에 어떤 함수를 쓸건지, aggfunc = 'size' 크기, 다시 말해 갯수를 지정해서 만듦
print(table)


# In[18]:


sns.heatmap(table, annot = True, fmt ='d', cmap = "YlGnBu", linewidth = .5, cbar = False) 
# -> 히트맵에 사용되어야 할 데이터를 첫번째 매개변수에 전달, 
# 데이터에 대한 각각의 값을 히트맵에 표시할지를 두번째 매개변수(annot)에 지정,
# 포맷을 어떻게 값을 지정해서 보여줄거냐를 세번째 매개변수(fmt)에 지정, 'd': 정수값으로 표현
# 히트맵에 들어갈 하나의 단위가 되는 셀의 색 지정을 네번째 매개변수(cmap)에 지정, 노초파 계열로 해서 각 누적 카운트 부분만큼 보여줌
# colorbar 색 지정을 다섯번째 매개변수에 지정
plt.show()


# In[19]:


sns.heatmap(table, annot = True, fmt ='d', cmap = "YlGnBu", linewidth = .5, cbar = True) 
plt.show()


# In[20]:


# 범주형 데이터의 산점도

# 클래스별로 데이터가 얼마만큼 분포가 되어있는지를 특정한 또다른 변수 나이에 따라서 표시. 
# 요약된 정보가 아니라 각각의 데이터가 흝어져있는 거를 있는 그대로 산점도로 표시된걸 보여줄것임
# 메소드: stripplot, swarmplot


# In[21]:


sns.set_style('whitegrid')


# In[22]:


# 두 개를 비교하기 위해 subplot 만들어줌
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

# 산점도 그래프는 클래스 자체에 대해서 흝어진 정보를 연속된 데이터처럼 그림
sns.stripplot(x = 'class', y = 'age', data = titanic, ax = ax1) 
# -> 1,2,3등석의 나이대가 어떻게 분포되어 있는지 확인 가능, 밀집도의 정확한 파악이 어려움
# 해당 클래스별로 산점도가 나옴(마치 산점도 그래프를 3개 그리는것처럼)
sns.swarmplot(x = 'class', y = 'age', data = titanic, ax = ax2) 
plt.show()


# In[23]:


# 막대그래프
# 특정한 변수(columns)를 할당해서 그림, 해당되는 변수에 값을 새로운 값 추가. 

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

sns.barplot(x = 'sex', y = 'survived', data = titanic, ax = ax1)
sns.barplot(x = 'sex', y = 'survived', hue = 'class', data = titanic, ax = ax2)
# -> hue라는 메소드에 class로 분류해서 막대그래프로 그려라
sns.barplot(x = 'sex', y = 'survived', hue = 'class', dodge = False, data = titanic, ax = ax3)
# -> 클래스별로 구분을 하는데 별도의 막대그래프로 보여주지 않고 누적 형태로 출력
plt.show()


# In[24]:


# countplot으로 그래프 그리기
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
# 왼쪽부터 1,2,3 영역에 각각 그래프를 그리게 설정
sns.countplot(x = 'class', data = titanic, ax = ax1) 
# 타이타닉 데이터 중에서 클래스 열을 가져와 사용. 1등석, 2등석, 3등석 3개로 분류 / 빈도그래프 출력 위치
sns.countplot(x = 'class', hue = 'who', data = titanic, ax = ax2) # hue로 막대그래프가 세부적으로 쪼개짐
sns.countplot(x = 'class', hue = 'who', data = titanic, ax = ax3, dodge = False) # 누적형태로 하나의 막대그래프에 쌓게
plt.show()


# In[25]:


# 바이올린 그래프: 분포 정보를 더 추가해서 한 화면에서 볼 수 있게 제공, 박프플롯이 커널 밀도 함수로 표현됨

fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,2,1) # 2*2 4개 만들기
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
sns.boxplot(x = 'alive', y = 'age', data = titanic, ax = ax1)
sns.boxplot(x = 'alive', y = 'age', hue = 'sex', data = titanic, ax = ax2)
sns.violinplot(x = 'alive', y = 'age', data = titanic, ax = ax3)
sns.violinplot(x = 'alive', y = 'age', hue = 'sex', data = titanic, ax = ax4)
plt.show()


# In[26]:


# 조인트그래프: 산점도 형태로 표시됨 , 각 변수에 대한 히스토그램, 전체 각 구간 별 누적한 데이터의 빈도를 커널 밀도 함수로 그림
# 각각의 x축, y축에 있는 데이터 분포가 히스토그램을 보완해서 볼 수 있음
sns.jointplot(x = 'fare', y = 'age', data = titanic)
plt.show()


# In[27]:


sns.jointplot(x = 'fare', y = 'age', data = titanic)
sns.jointplot(x = 'fare', y = 'age', kind = 'reg', data = titanic) # 회귀값 추가(reg)
sns.jointplot(x = 'fare', y = 'age', kind = 'hex', data = titanic) # 육각형 모양으로 색깔로 밀집도를 알 수 있음
sns.jointplot(x = 'fare', y = 'age', kind = 'kde', data = titanic)
plt.show()


# In[28]:


# 그리드 분할
# grid: 가로,세로 나눠서 표현 , 특정 조건을 갖고 여러개의 subplot을 만들어주는 메소드가 제공됨. 
# subplot을 구성하지 않아도 자동으로 채움
g = sns.FacetGrid(data = titanic, col = 'who', row = 'survived') # col: 열, row: 행
g = g.map(plt.hist, 'age') # 나이의 분포를 히스토그램으로


# In[34]:


# 이변수 데이터 분포: 2개씩 조합할 수 있는 형태의 그래프를 원한다
# 지정된 열을 2개씩 짝지어서 자동으로 그래프를 그림
# 특정한 리스트를 만들어서 전달하면 알아서 해당 리스트 상에 두 개의 변수들 사이에 그래프를 자동으로 subplot에 만듦
a = titanic[['age', 'pclass', 'fare']]
g = sns.pairplot(a)


# In[ ]:




