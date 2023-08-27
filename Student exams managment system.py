# import random function.
import random
# Create List of subjects.
# i am using a list of total 12 subjects.
subjects = ["Math", "Science", "English", "History", "Geography", "Biology",
            "Physics", "Chemistry", "Computer Science", "Art", "Music", "PE"]
# Creating a Empty List where later we save our matching students.
matching_students = []

# Creating our 10 Students list.
for i in range(1, 11):
    # Creating a new variable named as student and assigning it value in the form of "student 1".
    student = "Student" + str(i)
    # Creating a new variable named as "subj" and selecting 3 random subjects
    # and saving them in subj.
    subj = random.sample(subjects, 3)
    # Adding subjects with the students names and saving them in a new vaiable.
    student_subjects = [student] + subj
    # printing the combination of both student names and randomly selected subjects.
    print(student_subjects)
# A foor loop j where range starts from 1 to i.
    for j in range(1, i):
        # Creating a variable and assigning it the value with 1+.
        prev_student = "student" + str(j)
        prev_subj = student_subjects[1:]
        # Checking if the subj is eqal to prev_subj.
        if subj == prev_subj:
            # Adding matching students in matching students list.
            matching_students.append((student, prev_student))
# Printing the results.
print("These students can give exams together\n", matching_students)