import datetime
import time
import os
import glob
print(glob.glob("*.py"))

print(os.getcwd())

folder = "sample_dir"

if os.path.exsist(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print(folder, "폴더를 삭제하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")


print(os.listdir())
print(time.localtime())
print(time.strftime("%y-%m-%d %h:%m:%s"))

print("오늘 날짜는 ", datetime.date.today())
today = datetime.date.today()
td = datetime.timedelta(days=100)
print("우리가 만난지 100일은", today + td)
