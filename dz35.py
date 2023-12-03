class TooManyStudentsErrorGroup(Exception):
    pass


class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years old, {self.gender}'


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f', Record Book: {self.record_book}'


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise TooManyStudentsErrorGroup("Cannot add more than 10 students to the group.")
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_remove = self.find_student(last_name)
        if student_to_remove:
            self.group.remove(student_to_remove)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'


# Код для тестування
st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 28, 'Mark', 'Zuckerberg', 'AN146')
st4 = Student('Female', 24, 'Emma', 'Watson', 'AN147')
st5 = Student('Male', 32, 'Elon', 'Musk', 'AN148')
st6 = Student('Female', 22, 'Taylor', 'Swift', 'AN149')
st7 = Student('Male', 29, 'Bill', 'Gates', 'AN150')
st8 = Student('Female', 26, 'Adele', 'Adkins', 'AN151')
st9 = Student('Male', 31, 'Jeff', 'Bezos', 'AN152')
st10 = Student('Female', 23, 'Selena', 'Gomez', 'AN153')
st11 = Student('Male', 33, 'Kanye', 'West', 'AN154')

gr = Group('PD1')

try:
    for student in [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]:
        gr.add_student(student)
except TooManyStudentsErrorGroup as e:
    print(f"Error: {e}")

print(gr)
