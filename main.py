class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        print()
        print(f"문제: {self.question}")
        for i in range(len(self.choices)):
            print(f"  {i + 1}. {self.choices[i]}")

    def is_correct(self, user_answer):
        return user_answer == self.answer


def create_default_quizzes():
    quizzes = [
        Quiz(
            "대전의 옛 순우리말 이름은?",
            ["새벌", "한밭", "푸른들", "큰고을"],
            2,
        ),
        Quiz(
            "대전의 유명 빵집 성심당의 대표 메뉴로 꼽히는 것은?",
            ["튀김소보로", "호두과자", "붕어빵", "찐빵"],
            1,
        ),
        Quiz(
            "대전에 있는 유명한 온천 지역은?",
            ["덕산", "온양", "유성", "수안보"],
            3,
        ),
        Quiz(
            "1993년에 대전에서 열린 국제 행사는?",
            ["서울 올림픽", "한일 월드컵", "부산 아시안게임", "대전 엑스포"],
            4,
        ),
        Quiz(
            "대전의 3대 하천이 아닌 것은?",
            ["갑천", "섬진강", "유등천", "대전천"],
            2,
        ),
    ]
    return quizzes


def show_menu():
    print()
    print("=" * 30)
    print("   파이썬 퀴즈 게임")
    print("=" * 30)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("=" * 30)


def main():
    while True:
        show_menu()

        try:
            choice = input("번호를 선택하세요: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 안전하게 종료합니다. 안녕히 가세요!")
            break

        if choice == "":
            print("아무것도 입력하지 않았어요. 1~5 사이의 번호를 입력해 주세요.")
            continue

        try:
            number = int(choice)
        except ValueError:
            print("숫자만 입력할 수 있어요. 1~5 사이의 번호를 입력해 주세요.")
            continue

        if number == 1:
            print("퀴즈 풀기 기능은 아직 준비 중이에요.")
        elif number == 2:
            print("퀴즈 추가 기능은 아직 준비 중이에요.")
        elif number == 3:
            print("퀴즈 목록 기능은 아직 준비 중이에요.")
        elif number == 4:
            print("점수 확인 기능은 아직 준비 중이에요.")
        elif number == 5:
            print("게임을 종료합니다. 안녕히 가세요!")
            break
        else:
            print("1~5 사이의 번호만 선택할 수 있어요.")


if __name__ == "__main__":
    main()