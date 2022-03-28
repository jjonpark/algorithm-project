# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10 자리 확보
print("{0:>10}".format(500))

#3자리마다 콤마 찍어주기 
print("{0:,}".format(1000000000000))
#소수점 출력 (소수점 3쨰 자리에서 반올림)
print("{0:.2f}".format(5/3))


# import pickle
# profile_file =open("profile.pickle", "wb")

#class 공부

#마린 : 공격 유닛, 군인, 총을 쏠수 있음
name = "마린"
hp = 40
damage = 5 #유닛의 공격력
print("{0} 유닛이 생성되었습니다. ". format(name))
print("체력 {0}, 공격력 {1} \n" .format(hp, damage))

class unit :
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp =hp
        self.damage=damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1} ".format(self.hp, self.damage))
    
marine1 =unit("마린", 40, 5)
marine2 = unit("마린2",40,5)
tank = unit("탱크",150,35)

#출력 예제 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제 )
# 총 3대의 아파트 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

class House :
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price 
        self.completion_year = completion_year 

    def show_detail(self) : 
        print(self.location, self.house_type, self.deal_type, self.price, self.completion_year)

houses = []
house1 =House("강남","아파트", "매매", "10억" , "2010년")
house2 = House("마포","오피스텔","전세","5억", "2007년") 

houses.append(house1)
houses.append(house2)

print("총 {0}대의 매물이 있습니다. ".format(len(houses)))

for house in houses:
    house.show_detail()


    