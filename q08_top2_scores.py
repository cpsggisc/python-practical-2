# Finding the two highest scores

students = {}

studentcount = int(input("Enter number of students: "))

for i in range(studentcount):
    names = (input("Enter student name: "))
    scores = (int(input("Enter score: ")))
    students[names] = scores

keys = sorted(students.items(), key=lambda scores: scores[1])
print("Highest scorer and score is",keys[studentcount-1])
print("Second highest scorer and score is",keys[studentcount-2])

    





    





