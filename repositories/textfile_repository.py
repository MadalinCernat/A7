from student import Student
from .base_repository import *

class TextFileRepository(BaseRepository):
    def __init__(self, file_name):
        super(TextFileRepository, self).__init__()
        self._file_name = file_name

    def add(self, student: Student):
        students = self.get_all()
        
        search = self.find_by_id(student.get_id())

        if search is None:
            students.append(student)
        else:
            raise ValueError("Id already taken!")

        self.write(students)

    def find_by_id(self, student_id):
        students = self.get_all()
        students = list(filter(lambda x: (x.get_id() == student_id), students))
        if len(students) > 0:
            student = students[0]
        return student

    def remove_by_id(self, student_id):
        students = self.get_all()
        students = list(filter(lambda x: (x.get_id() != student_id), students))
        self.write(students)

    def remove_all(self):
        open(self._file_name, 'w').close()

    def get_all(self):
        output = []
        file = open(self._file_name, 'r')

        lines = file.read()
        lines = lines.splitlines()
        for l in lines:
            values = l.split(',')
            student = Student(values[0], values[1], values[2])
            output.append(student)

        file.close()
        return output

    def write(self, students: list):
        file = open(self._file_name, "w")

        lines = self.split_in_lines(students)

        for l in lines:
            file.write(l)
            file.write("\n")

        file.close()

    def split_in_lines(self, students: list):
        lines = []
        for s in students:
            lines.append(f"{s.get_id()},{s.get_name()},{s.get_group()}")
        return lines