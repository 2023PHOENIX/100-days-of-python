student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
StudentGrade = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for student in student_scores:
    if student_scores[student] >= 91:
        StudentGrade[student] = "Outstanding"
    elif 81 <= student_scores[student] < 91:
        StudentGrade[student] = "Exceeded Expectations"
    elif 71 <= student_scores[student] < 81:
        StudentGrade[student] = "Accepted Expectations"
    else:
        StudentGrade[student] = "Fail Better luck next time"



print(StudentGrade)
