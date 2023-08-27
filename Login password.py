import random

# Create a list of 12 subjects
subjects = ["Math", "Science", "English", "History", "Geography", "Biology",
            "Physics", "Chemistry", "Computer Science", "Art", "Music", "PE"]

# Create a list to store the students with matching subjects
matching_students = []

# Use a loop to generate a list of students
for i in range(1, 11):
    student = "student" + str(i)
    # Randomly select 3 subjects for the current student
    subj = random.sample(subjects, 3)
    # Create a list for the current student and their subjects
    student_subjects = [student] + subj
    # Print the list
    print(student_subjects)
    # Use another loop to check the subjects of the current student with the subjects of the previous students
    for j in range(1, i):
        prev_student = "student" + str(j)
        prev_subj = student_subjects[1:]
        # Compare the subjects of the current student with the subjects of the previous students
        if subj == prev_subj:
            # If the subjects match, add the student names to the matching_students list
            matching_students.append(student)

# Remove duplicate entries and iterate through matching_students list
for student in set(matching_students):
    for student2 in set(matching_students):
        if student != student2:
            print(student, student2)

