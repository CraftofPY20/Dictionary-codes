student_scores ={
    "Akwasi" : 35,
    "Kwame" : 75,
    "Mercy" : 90,
    "Judith" : 45,
}
name = input("Enter the name of the student: ")
if name in student_scores:
    if student_scores[name] < 50:
        print(name, "has failed the exam.")
    else:
        print(name, "has passed the exam.")
else:
    print("Student not found in the dictionary.")