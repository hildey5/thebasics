student_grades = [9.1, 8.8, 7.5]

student_grades = {"Marry": 9.1, "Josh":8.8, "Mike": 7.5, "Lucas": 2.1}

mysum = sum(student_grades.values())
length = len(student_grades)

mean = mysum / length 

print(mean)

for key, value in student_grades.items():
    if value < 5.0:
        print("Student", key, "needs to study more because he failed with a mark of", value)
        if key == "Lucas":
            print("But he has an awesome Dad!")