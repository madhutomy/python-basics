# Average height of a list of persons

# Input a Python list of student heights
student_heights = input().split()
total_height = 0
no_students = len(student_heights)
for n in range(0, no_students):
    total_height += int(student_heights[n])

print(f"total height = {total_height}")
print(f"number of students = {no_students}")
print(f"average height = {round(total_height / no_students)}")
