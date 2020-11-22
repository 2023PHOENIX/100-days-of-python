from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    newQuestion = Question(q_text=question_text, q_ans=question_answer)
    question_bank.append(newQuestion)

quiz = QuizBrain(question_bank)
while quiz.is_question_left:
    quiz.next_question()


