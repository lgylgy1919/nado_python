gun = 10


def checkpoint(soliders):
    global gun  # 전역 변수 gun을 사용
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))


def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
checkpoint(2)
# [함수 내] 남은 총 : 8
gun = checkpoint_ret(gun, 2)
# [함수 내] 남은 총 : 6
print("남은 총 : {0}".format(gun))
# 남은 총 :6
