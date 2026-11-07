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