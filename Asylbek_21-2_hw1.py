class Person:

    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Fullname: {self.fullname} Age: {self.age} Is married: {self.is_married}')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks:dict):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_marks(self):
        print(round(sum(self.marks.values())/len(self.marks), 2))

class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, expirience):
        super().__init__(fullname, age, is_married)
        self.expirience = expirience

    def calc_salary(self):
        self.salary = round(self.salary + (self.salary/100*5 * max(0, self.expirience-3)), 0)
        return self.salary

def create_students():
    students = []
    students.append( Student('Almaz', 17, False, {'Math':2, 'Physical Edu.':5, 'Russian':3}) )
    students.append( Student('Asylbek', 17, False, {'Math':5, 'Geography':5, 'Biology':4}) )
    students.append( Student('Marlen', 17, False, {'All':2}) )
    return students


Aleksay = Teacher('Aleksey', 40, False, 5)
Aleksay.introduce_myself()
print(Aleksay.calc_salary())

students = create_students()

for student in students:
    student.introduce_myself()
    for subject,mark in student.marks.items():
        print(f'{subject}: {mark}', end="; ")
    student.average_marks()