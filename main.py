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


def read_number(prompt, min_value, max_value):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("아무것도 입력하지 않았어요. 숫자를 입력해 주세요.")
            continue

        try:
            number = int(text)
        except ValueError:
            print("숫자만 입력할 수 있어요.")
            continue

        if number < min_value or number > max_value:
            print(f"{min_value}~{max_value} 사이의 숫자만 입력할 수 있어요.")
            continue

        return number


def read_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("아무것도 입력하지 않았어요. 내용을 입력해 주세요.")
            continue

        return text


def play_quiz(quizzes):
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없어요. 먼저 퀴즈를 추가해 주세요.")
        return None

    total = len(quizzes)
    score = 0
    print(f"\n퀴즈를 시작합니다! 총 {total}문제예요.")

    for i in range(total):
        quiz = quizzes[i]
        print(f"\n[{i + 1}/{total}]")
        quiz.show()

        max_choice = len(quiz.choices)
        user_answer = read_number(f"정답 번호를 입력하세요 (1~{max_choice}): ", 1, max_choice)

        if quiz.is_correct(user_answer):
            print("정답이에요!")
            score += 1
        else:
            right_text = quiz.choices[quiz.answer - 1]
            print(f"틀렸어요. 정답은 {quiz.answer}번 '{right_text}' 이에요.")

    print()
    print("=" * 30)
    print(f"결과: {total}문제 중 {score}문제를 맞혔어요!")
    print("=" * 30)
    return score


def add_quiz(quizzes):
    print("\n새 퀴즈를 추가합니다.")
    question = read_text("문제를 입력하세요: ")

    choices = []
    for i in range(4):
        choice = read_text(f"선택지 {i + 1}번을 입력하세요: ")
        choices.append(choice)

    answer = read_number("정답 번호를 입력하세요 (1~4): ", 1, 4)

    new_quiz = Quiz(question, choices, answer)
    quizzes.append(new_quiz)
    print("퀴즈가 추가되었어요!")
    print(f"현재 퀴즈는 모두 {len(quizzes)}개예요.")


def show_quiz_list(quizzes):
    if len(quizzes) == 0:
        print("등록된 퀴즈가 없어요.")
        return

    print()
    print("=" * 30)
    print(f"   퀴즈 목록 (총 {len(quizzes)}개)")
    print("=" * 30)

    for i in range(len(quizzes)):
        quiz = quizzes[i]
        print(f"\n{i + 1}. {quiz.question}")
        for j in range(len(quiz.choices)):
            print(f"   {j + 1}) {quiz.choices[j]}")
        print(f"   정답: {quiz.answer}번")


def update_best_score(best_score, new_score):
    if best_score is None:
        print(f"첫 기록이에요! 최고 점수는 {new_score}점이에요.")
        return new_score

    if new_score > best_score:
        print(f"새 최고 점수예요! ({best_score}점 -> {new_score}점)")
        return new_score

    print(f"이번 점수는 {new_score}점이에요. 최고 점수는 그대로 {best_score}점이에요.")
    return best_score


def show_best_score(best_score):
    if best_score is None:
        print("아직 퀴즈를 풀지 않았어요. 먼저 퀴즈를 풀어보세요!")
    else:
        print(f"현재 최고 점수는 {best_score}점이에요.")


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
    quizzes = create_default_quizzes()
    best_score = None

    try:
        while True:
            show_menu()
            number = read_number("번호를 선택하세요: ", 1, 5)

            if number == 1:
                score = play_quiz(quizzes)
                if score is not None:
                    best_score = update_best_score(best_score, score)
            elif number == 2:
                add_quiz(quizzes)
            elif number == 3:
                show_quiz_list(quizzes)
            elif number == 4:
                show_best_score(best_score)
            elif number == 5:
                print("게임을 종료합니다. 안녕히 가세요!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\n프로그램을 안전하게 종료합니다. 안녕히 가세요!")


if __name__ == "__main__":
    main()