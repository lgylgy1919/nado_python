def profile_(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t 나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language):
    print("이름: {0}\t 나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")


profile("유재석", 20, "Python", "Java", "C", "C#", "C++", "javascript")
profile("김태호", 30, "Kotlin", "Swift", "", "", "")
