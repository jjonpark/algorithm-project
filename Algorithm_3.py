#백준 문제 풀이 로마 숫자 
    # x_1=list(str(input()))
    # x_2=list(str(input()))

    # def roma_to_num(x:list) ->int:
    #     result=0
    #     list={"I":1,"V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    #     result+=list[x[0]]
    #     for i in range(1,len(x)):
    #         if x[i] in list.keys():
    #             result+=list[x[i]]
    #         if list[x[i-1]] < list[x[i]]:
    #             result -=(list[x[i-1]]*2)
    #     result=int(result)
    #     return result

    # def num_to_roma(n:int)->str:
    #     s=""
    #     while n>0:
    #         if n>=1000:
    #             s+="M"
    #             n-=1000
    #         elif n>=900:
    #             s+="CM"
    #             n-=900
    #         elif n>=500:
    #             s+="D"
    #             n-=500
    #         elif n>=400:
    #             s+="CD"
    #             n-=400
    #         elif n>=100:
    #             s+="C"
    #             n-=100
    #         elif n>=90:
    #             s+="XC"
    #             n-=90
    #         elif n>=50:
    #             s+="L"
    #             n-=50
    #         elif n>=40:
    #             s+="XL"
    #             n-=40
    #         elif n>=10:
    #             s+="X"
    #             n-=10
    #         elif n>=9:
    #             s+="IX"
    #             n-=9
    #         elif n>=5:
    #             s+="V"
    #             n-=5
    #         elif n>=4:
    #             s+="IV"
    #             n-=4
    #         elif n>=1:
    #             s+="I"
    #             n-=1
    #     return s

    # answer_num= (roma_to_num(x_1) + roma_to_num(x_2))
    # print(answer_num)
    # print(num_to_roma(answer_num))

#백준 알고리즘 <패션왕 신해빈>
T=int(input())
for test_case in range(1,T+1):
    x=int(input())
    kinds_list={}
    num_list=[]
    for i in range(x):
        K_1,K_2=map(str,input().split())
        if K_2 in kinds_list.keys():
            for i in range(len(num_list)):
                if(K_2==num_list[i][0]):
                    num_list[i][1]+=1
        else:
            kinds_list[K_2]=K_1
            num_list.append([K_2,1])
    result=1
    for i in range(len(num_list)):
        result*=(num_list[i][1]+1)
    print(result-1)
