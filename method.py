# 메소드

class Unit: # Unit이라는 클래스를 만듦
    def __init__(self, name, hp, damage):
        self.name = name # 필요한 값들을 정의 해줌
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))

# 공격 유닛
class AttackUnit:
    def __init__(self, name, hp, damage): # 함수
        self.name = name # self.name을 통해서 자기 자신의 변수에 접근할 수 있음, 우변의 name은 위에 있는 name에서 전달 받은 인자를 바로 쓴다는 의미
        self.hp = hp
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

# 파이어뱃: 공격 유닛, 화염방사기.
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)



       
