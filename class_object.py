class student:
    roll = ""
    gpa = ""
rahim = student()
print(isinstance(rahim,student))
rahim.roll = 101
rahim.gpa = 3.75
print(f"Roll : {rahim.roll}, GPA :{rahim.gpa}")