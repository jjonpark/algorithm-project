#예외처리

# try : 
#     print("나누기 전용 계산기 입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요 : "))
#     num2 = int(input("두번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1,num2, int(num1/num2)))

# except ValueError :
#     print("에러! 잘못된 값을 입력하였습니다. ")
# except ZeroDivisionError as err :
#     print(err)

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 떄는 ValueError 로 처리 
#         출력 메세지 : "잘못된 값을 입력하였습니다"
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량은 10마리로 한정 
#         치킨 소진 시 사용자 정의 에러 [soldout error]를 발생시키고 프로그램 종료
#         출력 메시지 : "재고가 소진되어 더 이상 주문을 받이 않습니다."

# class SoldoutError(Exception):
#     pass

# chicken = 10
# waiting = 1
# while(True) :
#     try :
#         print("남은치킨 : {0} ".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까? "))
#         if order > chicken :
#             print("재료가 부족합니다. ")
#         elif order <= 0:
#             raise ValueError
#         else :
#             print("대기번호 {0}번 손님 주문하신 치킨 {1}마리가 완료되었습니다." .format(waiting, order))
#             waiting += 1
#             chicken -= order
#         if chicken ==0 :
#             raise SoldoutError
#     except ValueError :
#         print("잘못된 값을 입력하였습니다.")
#     except SoldoutError :
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break
#모듈은 py 의 확장자 명을 가지며, from ~~~ import * 을 통해 안에 있는 함수를 사용할수 있다.
