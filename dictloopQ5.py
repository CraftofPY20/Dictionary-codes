student_scores = {
    "John" : 85,
    "Mary" : 62,
    "Peter" : 48,
    "Kate" : 90
}
for student, score in student_scores.items():
    if score >= 50:
        print(student, ":", score)
    
