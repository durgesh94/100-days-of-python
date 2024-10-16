student_scores = [92, 67, 85, 76, 48, 55, 99, 42, 73, 89, 60, 81, 78, 95, 37, 88, 63, 54, 74, 91]

sum_score = 0
max_score = 0
for score in student_scores:
    sum_score += score
    if max_score < score:
        max_score = score
print(f"sum of score: {sum_score}")
avg_score = sum_score / len(student_scores)
print(f"average of score: {avg_score}")
print(f"max score: {max_score}")
