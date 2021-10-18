from data import question_data
from question_model import Question
from quiz_begin import QuizBrain

#
question_bank = []
#go on to data.py, iterate over the list of items
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    #created a new object with Question class (quiz_model.py)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank) #Quiz_brain class in quiz_begin.py
while quiz.still_has_questions():
    quiz.next_question()
    print("\n")

print('you are successfully completed this game🎉')
print(f'your final score is{quiz.score}/{len(question_bank)}')