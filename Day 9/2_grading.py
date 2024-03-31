students = {
    "nisha": 97,
    "suman": 89,
    "prerana": 78,
    "rajashree": 56
}
# a = input("Enter Your Name: ")
# print(students[a])
# if ((students[a]) < 100) and ((students[a]) > 90):
#     print("Your score is outstanding")
# if ((students[a]) < 90) and ((students[a]) > 80):
#     print("Your score Exceeds Expectation")
# if ((students[a]) < 80) and ((students[a]) > 70):
#     print("Your score is Acceptable")
# if ((students[a]) < 70):
#     print("You Failed")

student_grade = {}
for student in students:
    score = students[student]
    if score > 90:
        students[student] = "outstanding"
    elif score > 80:
        students[student] = "Exceeds Expectation"
    elif score > 70:
        students[student] = "Acceptable"
    else:
        students[student] = "Fail"
print(students)
