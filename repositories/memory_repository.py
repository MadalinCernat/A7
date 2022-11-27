from student import Student
from .base_repository import *

class MemoryRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self._students = []


    def add(self, student: Student):
        self._students.append(student)

    def remove_by_id(self, student_id):
        self._students= list(filter(lambda x: (x.get_id() != student_id), self._students))

    def remove_all(self):
        self._students.clear()

    def find_by_id(self, student_id):
        students = list(filter(lambda x: (x.get_id() == student_id), self._students))
        student = None
        if len(students) > 0:
            student = students[0]
        return student

    def get_all(self):
        return self._students