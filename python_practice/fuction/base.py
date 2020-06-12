def profile(name, age, main_lang):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile("이재윤", 20, "python")
profile("김태호", 40, "java")


def profile_(name, age=17, main_lang="python"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}"
          .format(name, age, main_lang))


profile_("이재윤")
profile_("김태호")
