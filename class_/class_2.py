class Unit:
    def __init__(self, name, hp, damage):
        # 멤버 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력{1}".format(self.hp, self.damage))


# <클래스로부터 만들어지는 대상을 객체라 한다.>
# <마린과 탱크는 Unit클래스의 instance>
marine1 = Unit("마린1", 40, 5)
# => 마린1 유닛이 생성 되었습니다.
# => 체력 40, 공격력 5
marine2 = Unit("마린2", 40, 5)
# => 마린2 유닛이 생성되었습니다.
# => 체력 40, 공격력 5
tank = Unit("탱크", 150, 35)
# => 탱크 유닛이 생성되었습니다.
# => 체력 150, 공격력 35


# <외부에서 멤버변수를 사용가능>
wraith1 = Unit("레이스", 80, 5)
# => 레이스 유닛이 생성되었습니다.
# => 체력 80, 공격력 5
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))
# => 유닛 이름 : 레이스, 공격력 5


# <clocking 변수를 외부에서 추가로 할당>
wraith2 = Unit("빼앗은 레이스", 80, 5)
# => 빼앗은 유닛이 생성되었습니다.
# => 체력 80, 공격력 5
wraith2.clocking = True

if wraith2.clocking == True:
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
# => 빼앗은 레이스는 현재 클로킹 상태입니다.
