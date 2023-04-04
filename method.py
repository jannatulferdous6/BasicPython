class student:
    roll = ""
    gpa = ""

    def set_value(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa
        

    def display(self):
        print(f"Roll : {self.roll}, GPA :{self.gpa}")

rahim = student()
karim = student()
print(isinstance(rahim,student))


# rahim.roll = 101
# rahim.gpa = 3.75
rahim.set_value(101, 3.75)
rahim.display()

karim.roll = 102
karim.gpa = 3.05
karim.display()
print(f"Roll : {karim.roll}, GPA :{karim.gpa}")