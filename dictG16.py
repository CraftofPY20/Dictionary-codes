student_scores ={
    "Akwasi" : 35,
    "Kwame" : 75,
    "Mercy" : 90,
    "Judith" : 45,
}
highest_score = max(student_scores.values())
for student, score in student_scores.items():
    if score == highest_score:
        print(student, "has the highest score")
    