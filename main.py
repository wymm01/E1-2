import json
import os

STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")


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

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }


class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = None
        self.load_state()

    def create_default_quizzes(self):
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

    def dict_to_quiz(self, data):
        question = data["question"]
        choices = data["choices"]
        answer = data["answer"]

        if not isinstance(question, str) or question.strip() == "":
            raise ValueError("문제가 올바르지 않아요.")

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 4개여야 해요.")

        for choice in choices:
            if not isinstance(choice, str):
                raise ValueError("선택지가 올바르지 않아요.")

        if not isinstance(answer, int) or isinstance(answer, bool):
            raise ValueError("정답 번호가 올바르지 않아요.")

        if answer < 1 or answer > 4:
            raise ValueError("정답 번호는 1~4여야 해요.")

        return Quiz(question, choices, answer)

    def load_state(self):
        if not os.path.exists(STATE_FILE):
            print("저장된 파일이 없어서 기본 퀴즈로 시작해요.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = None
            return

        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)

            loaded_quizzes = []
            for item in data["quizzes"]:
                loaded_quizzes.append(self.dict_to_quiz(item))

            loaded_best_score = data["best_score"]
            if loaded_best_score is not None:
                if not isinstance(loaded_best_score, int) or isinstance(loaded_best_score, bool):
                    raise ValueError("최고 점수가 올바르지 않아요.")
                if loaded_best_score < 0:
                    raise ValueError("최고 점수가 올바르지 않아요.")

            self.quizzes = loaded_quizzes
            self.best_score = loaded_best_score
            print("저장된 파일에서 퀴즈와 점수를 불러왔어요.")
        except (OSError, ValueError, KeyError, TypeError):
            print("저장 파일을 읽을 수 없거나 손상되었어요. 기본 퀴즈로 초기화할게요.")
            self.quizzes = self.create_default_quizzes()
            self.best_score = None
            self.save_state()

    def save_state(self):
        quiz_list = []
        for quiz in self.quizzes:
            quiz_list.append(quiz.to_dict())

        data = {
            "quizzes": quiz_list,
            "best_score": self.best_score,
        }

        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except OSError:
            print("파일을 저장하지 못했어요. 이번에 바꾼 내용은 프로그램을 끄면 사라질 수 있어요.")

    def read_number(self, prompt, min_value, max_value):
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

    def read_text(self, prompt):
        while True:
            text = input(prompt).strip()

            if text == "":
                print("아무것도 입력하지 않았어요. 내용을 입력해 주세요.")
                continue

            return text

    def show_menu(self):
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

    def play_quiz(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없어요. 먼저 퀴즈를 추가해 주세요.")
            return None

        total = len(self.quizzes)
        score = 0
        print(f"\n퀴즈를 시작합니다! 총 {total}문제예요.")

        for i in range(total):
            quiz = self.quizzes[i]
            print(f"\n[{i + 1}/{total}]")
            quiz.show()

            max_choice = len(quiz.choices)
            user_answer = self.read_number(
                f"정답 번호를 입력하세요 (1~{max_choice}): ", 1, max_choice
            )

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

    def add_quiz(self):
        print("\n새 퀴즈를 추가합니다.")
        question = self.read_text("문제를 입력하세요: ")

        choices = []
        for i in range(4):
            choice = self.read_text(f"선택지 {i + 1}번을 입력하세요: ")
            choices.append(choice)

        answer = self.read_number("정답 번호를 입력하세요 (1~4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("퀴즈가 추가되었어요!")
        print(f"현재 퀴즈는 모두 {len(self.quizzes)}개예요.")

    def show_quiz_list(self):
        if len(self.quizzes) == 0:
            print("등록된 퀴즈가 없어요.")
            return

        print()
        print("=" * 30)
        print(f"   퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("=" * 30)

        for i in range(len(self.quizzes)):
            quiz = self.quizzes[i]
            print(f"\n{i + 1}. {quiz.question}")
            for j in range(len(quiz.choices)):
                print(f"   {j + 1}) {quiz.choices[j]}")
            print(f"   정답: {quiz.answer}번")

    def update_best_score(self, new_score):
        if self.best_score is None:
            print(f"첫 기록이에요! 최고 점수는 {new_score}점이에요.")
            self.best_score = new_score
            self.save_state()
        elif new_score > self.best_score:
            print(f"새 최고 점수예요! ({self.best_score}점 -> {new_score}점)")
            self.best_score = new_score
            self.save_state()
        else:
            print(
                f"이번 점수는 {new_score}점이에요. "
                f"최고 점수는 그대로 {self.best_score}점이에요."
            )

    def show_best_score(self):
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았어요. 먼저 퀴즈를 풀어보세요!")
        else:
            print(f"현재 최고 점수는 {self.best_score}점이에요.")

    def run(self):
        try:
            while True:
                self.show_menu()
                number = self.read_number("번호를 선택하세요: ", 1, 5)

                if number == 1:
                    score = self.play_quiz()
                    if score is not None:
                        self.update_best_score(score)
                elif number == 2:
                    self.add_quiz()
                elif number == 3:
                    self.show_quiz_list()
                elif number == 4:
                    self.show_best_score()
                elif number == 5:
                    self.save_state()
                    print("저장하고 게임을 종료합니다. 안녕히 가세요!")
                    break
        except (KeyboardInterrupt, EOFError):
            self.save_state()
            print("\n저장하고 프로그램을 안전하게 종료합니다. 안녕히 가세요!")


def main():
    game = QuizGame()
    game.run()


if __name__ == "__main__":
    main()