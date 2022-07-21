import pandas as pd
import numpy as np
np.array([1, 2, 3, 4, 5])


# array 는 단일 타입으로 구성된다.
# arr=np.array([1,2,3,4], dtype=float)
# print(arr)

# 배열 데이터 타입 dype 의 종류 : int, float, str, bool
# arr = np.zeros(10, dtype=int)
# arr = np.ones((3, 5), dtype=float)
# arr = np.arange(0, 20, 2)  # 0부터 20까지 2개씩 건너뛰면서 가주세요
# arr = np.linspace(0, 1, 5)  # 0~1 까지, 5등분해서 채워주세요
# print(arr)


# 난수로 채워진 배열 만들기
# arr = np.random.random((2, 2))  # 2곱하기 2사이즈의 난수를 가져와주세요
# 평균이 0이고 표준편차가 1인 정규분포를 따르는 수중 2*2난수를 가져와주세요
# arr = np.random.normal(0, 1, (2, 2))

# 배열의 기초
# x2 = np.random.randint(10, size=(3, 4))
# x2.ndim  # 2
# x2.shape  # (3,4)
# x2.size  # 12
# x2.dtype  # dtype("int64")

# 찾고 잘라내기
# x = np.arange(7)
# x[3]
# x[7]
# x[0] = 10

# 모양 바꾸기
# x = np.arange(8)
# x.shape  # (8,)
# x2 = x.reshape((2, 4))  # ([[0,1,2,3], [4,5,6,7]])
# x2.shape

# 이어 붙이고, 나누고
# matrix = np.arange(4).reshape(2, 2)
# x2 = np.concatenate([matrix, matrix], axis=0)
# print(x2)

# matrix = np.arange(16).reshape(4, 4)
# upper, lower = np.split(matrix, [3], axis=1)

# array의 모든 원소에 5를 더해서 만드는 함수
# def add_five_to_array(values):
#     output = np.empty(len(values))
#     for i in range(len(values)):
#         output[i] = values[i]+5
#     return output


# values = np.random.randint(1, 10, size=5)
# print(add_five_to_array(values))

# values + 5  # 이렇게 사용해도 된다. 수행속도가 더 빠르다

# # 다차원 행렬에서도 적용가능하다.
# x = np.arange(4).reshape((2, 2))
# y = np.random.randint(10, size=(2, 2))
# x+y
# x-y

# 브로드 캐스팅
# 서로 shape이 다른 array 끼리 연산
# matrix = np.array([[2, 4, 2], [6, 5, 9], [9, 4, 7]])
# print(matrix + np.array([1, 2, 3]))

# print(np.arange(3).reshape((3, 1))+np.arange(3))

# 집계 함수
# x = np.arange(8).reshape((2, 4))
# np.sum(x)  # 28
# np.min(x)  # 0
# np.max(x)  # 7
# np.mean(x)  # 3.5

# x = np.arange(8).reshape((2, 4))
# np.sum(x, axis=0)  # array([4,6,8,10])
# np.sum(x, axis=1)  # array([6,22])


# pandas
data = pd.Series([1, 2, 3, 4])
print(data)

data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(data['b'])

# 데이터 프레임 - 여러개의 Series가 모여서 행과 열을 이루는 데이터

population_dict = {
    'korea': 5180,
    'japan': 12718,
    'china': 141500,
    'usa': 32676,
}

population = pd.Series(population_dict)

gdp_dict = {
    'korea': 169320000,
    'japan': 516700000,
    'china': 1409250000,
    'usa': 2041280000,
}

gdp = pd.Series(gdp_dict)
country = pd.DataFrame({
    'population': population,
    'gdp': gdp
})
print(country)

# datav프레임의 Series도 numpy array 처럼 연산자를 쓸수 있다.
gdp_per_capita = country['gdp'] / country['population']
country['gdp per capita'] = gdp_per_capita
print(country)
country.to_csv("./country.csv")
country.to_excel("country.xlsx")

# indexing / Slicing - loc : 명시적인 인덱스를 참조하는 인덱싱/슬라이싱
print()
print(country.loc['china'])

print()
print(country.loc['japan':'korea', :'gdp'])

# iloc : 파이썬 스타일 정수 인덱스 인덱싱/슬라이싱
print()
print(country.iloc[0])
print()
print(country.iloc[1:3, :2])

# DataFrame 새 데이터 추가 / 수정
dataframe = pd.DataFrame(columns=['이름', '나이', '주소'])
dataframe.loc[0] = ['임원균', '26', '서울']
dataframe.loc[1] = {'이름': '철수', '나이': '25', '주소': '인천'}
dataframe.loc[1, '이름'] = '영희'

print()
print(dataframe)

# dataframe에 새 칼럼 추가
dataframe['전화번호'] = np.nan
dataframe.loc[0, '전화번호'] = '01012341234'
print()
print(dataframe)

# 컬럼 선택하기
# 컬럼이름이 하나만 들어가 있다면 Series
# 리스트로 들어가 있다면 DataFrame

# 누락된 데이터 체크
# 듀토리얼에서 보는 데이터와 달리 현실의 데이터는 누락되어 있는 형태가 많다.
dataframe.isnull()
dataframe.notnull()

dataframe.dropna()  # -> 비어있는 데이터가 삭제되어 출력
dataframe['전화번호'] = dataframe['전화번호'].fillna('전화번호 없음')
print()
print(dataframe)

# numpy array에서 사용했던 연산자들을 활용할수 있다.
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
A+B
print(A.add(B, fill_value=0))
