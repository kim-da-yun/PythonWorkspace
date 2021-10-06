# Quiz
# 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# (출력 예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 매매 5억 2007년
# 송파 빌라 월세 500/50 2000년

# [코드]
class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location =location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type\
            , self.price, self.completion_year)

houses = []
house1 = House("강남", "아파트", "매매", "10억", "2010년")
house2 = House("마포", "오피스텔", "매매", "5억", "2007년")
house3 = House("송파", "빌라", "월세", "500/50", "2000년")

houses.append(house1)
houses.append(house2)
houses.append(house3) # 추가해주는 이유: show_detail을 통해서 매물 정보를 표시해야 되는데 house1,2,3을 각각 쇼디테일하면 귀찮으니깐 리스트에 넣어서 반복문을 통해서 일괄적으로 하려고 

print("총 {0}대의 매물이 있습니다.".format(len(houses))) # len으로 감싸주면 house안에 있는 객체가 몇개인지 갯수를 줌
for house in houses:
    house.show_detail()

