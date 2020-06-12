class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flyable 생성자")


# 처음 클래스만 상속이 된다.
class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()


dropship = FlyableUnit()


class FlyableUnit_2(Unit, Flyable):
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)


drowship = FlyableUnit_2()
