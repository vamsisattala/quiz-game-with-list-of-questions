class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"{self.question_number }Q: {current_question.text}(True / False) :")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer , c_answer):
        if user_answer.lower() == c_answer.lower():
            self.score += 1
            print('you got it right')
        else:
            print('thats wrong!!')

        print(f'the correct answer is {c_answer}')
        print(f'your score is {self.score}/{self.question_number}')

