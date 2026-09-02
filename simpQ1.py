student_info = {
    "name": "James",
    "age": 25,
    "course": "Computer Science",
    "grade": "A"
}
info_to_display = input("Enter the information you want to display (name, age, course, grade): ")
if info_to_display in student_info:
    print(student_info[info_to_display])