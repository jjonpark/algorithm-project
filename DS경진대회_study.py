import numpy as np
np.array([1,2,3,4,5])


#array 는 단일 타입으로 구성된다. 
# arr=np.array([1,2,3,4], dtype=float)
# print(arr)

# 배열 데이터 타입 dype 의 종류 : int, float, str, bool
arr=np.zeros(10, dtype=int)
arr=np.ones((3,5), dtype=float)
print(arr)