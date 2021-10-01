# 상속
# Unit이라는 클래스의 내용을 상속받아서 어택 유닛을 만듦 / 유닛에 있는 멤버 변수와 메소드는 그대로 어택유닛에서 사용 가능

# 일반 유닛
class Unit: # Unit이라는 클래스를 만듦
    def __init__(self, name, hp):
        self.name = name # 필요한 값들을 정의 해줌
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit): # 공격유닛은 일반유닛 클래스를 상속 받아서 만들어짐
    def __init__(self, name, hp, damage): # 유닛에서 만들어진 생성자(__init__)를 호출해줘서 이름과 체력을 정의할 수 있음
        Unit.__init__(self, name, hp)
        self.damage = damage 

    def attack(self, location): # 두 번째 함수, 들여쓰기로 인해 어택유닛에 포함된 함수임
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"\
            .format(self.name, location, self.damage)) # self는 자기 자신을 의미함, 클래스내에서 메소드 앞에 항상 self를 적어줘야 함 / self.~을 통해서 자기 자신의 변수에 접근할 수 있음,
                # 이름과 공격력은 클래스 자기 자신의 멤버 변수의 값을 출력하는 것, location은 전달 받은 위의 값을 쓴다.

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage # 체력 - 데미지
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕: 의무병



# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)



       
