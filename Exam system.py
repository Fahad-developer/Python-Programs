import random

subjects = ["Math", "Science", "English", "History", "Geography", "Biology",
            "Physics", "Chemistry", "Computer Science", "Art", "Music", "PE"]


matching_students = []


for i in range(1, 11):
    student = "student" + str(i)

    subj = random.sample(subjects, 3)

    student_subjects = [student] + subj

    print(student_subjects)

    for j in range(1, i):
        prev_student = "student" + str(j)
        prev_subj = student_subjects[1:]

        if subj == prev_subj:

            matching_students.append((student, prev_student))


print("These Students can give exams together\n", matching_students)
