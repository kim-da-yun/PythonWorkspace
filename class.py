# class

# 붕어빵 틀처럼 서로 연관이 있는 변수와 함수의 집합 정도로 이해하기

# 마린: 공격 유닛, 군인. 총을 쏠 수 있음 
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크: 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드 / 시즈 모드.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{0}: {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format( \
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

class Unit: # Unit이라는 클래스를 만듦
    def __init__(self, name, hp, damage): # 함수 def:
        self.name = name # 필요한 값들을 정의 해줌
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))
    
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# --------------------------------------------------------------------------------------------------------------

# __init__ 함수
 
# __init__: 파이썬에서 쓰이는 생성자로, marine, tank 같은 객체가 만들어질때 자동으로 호출되는 부분임
# 객체: marine, tank 같이 어떠한 클래스로부터 만들어지는 것, 이때 marine, tank는 Unit 클래스의 instance라고 표현함,
# 객체가 생성될 때는 기본적으로 Unit 함수에 정의된 갯수와 동일하게 해야됨(self는 제외하고)

# marine3 = Unit("마린") 결과: TypeError: __init__() missing 2 required positional arguments: 'hp' and 'damage'
# Unit 함수에 정의된 갯수만큼 항상 똑같이 보내주어야 객체를 만들 수 있음

# --------------------------------------------------------------------------------------------------------------

# 멤버 변수

# 클래스 내에서 정의된 변수고 그 변수를 가지고 초기화를 할 수 있고 실제로 쓸 수 있음
        # self.name 
        # self.hp 
        # self.damage 에서 name, hp, damage가 멤버 변수임

# 레이스: 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름: {0}, 공격력: {1}".format(wraith1.name, wraith1.damage)) # 클래스 외부에서 멤버 변수를 사용하기 위한 예제

# 마인드 컨트롤: 상대방 유닛을 내 것으로 만드는 것(빼앗음)
wraith2 = Unit("뺴앗은 레이스", 80, 5)
wraith2.clocking = True # clocking이라는 변수는 위에 클래스에 없음(name, hp, damage만 있음), 변수를 추가로 할당하고 True라는 값을 넣음, 파이썬에서는 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수 있음
# 레이스2에는 클로킹이 있는데 레이스1에는 변수가(name, hp, damage만 있음), 
# 그래서 레이스1에 if wraith1.clocking == True: print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))코드를 run하면 clocking이라는 변수가 없다면서 오류가 발생함

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 클래스 외부에서 내가 원하는 변수에 대해서 확장을 할 수 있고 그 확장된 변수는 내가 확장을 한 객체에 대해서만 적용이 되고 기존에 있던 다른 객체에는 적용이 안됨 


