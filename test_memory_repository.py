from repositories.memory_repository import *
from student import *

class memory_repo_tests:
    def test_add(self):
        repo = MemoryRepository()

        student = Student(1, "Test", 923)
        repo.add(student)

        students = repo.get_all()

        assert students[0] == student

    def test_get_all(self):
        repo = MemoryRepository()
        student1 = Student(1, "Test1", 923)
        student2 = Student(2, "Test2", 924)
        students_expected = [student1, student2]

        repo.add(student1)
        repo.add(student2)

        students_actual = repo.get_all()

        assert students_actual[0] == students_expected[0] and students_actual[1] == students_expected[1] 


    def test_find_by_id(self):
        repo = MemoryRepository()

        student = Student(1, "Test", 923)
        repo.add(student)

        found_student = repo.find_by_id(student.get_id())

        assert student == found_student

    def test_remove_all(self):
        repo = MemoryRepository()

        student = Student(1, "Test", 923)
        repo.add(student)

        repo.remove_all()

        students = repo.get_all()

        assert students == []

    def test_remove_by_id(self):
        repo = MemoryRepository()

        student = Student(1, "Test", 923)
        repo.add(student) 

        repo.remove_by_id(student.get_id())

        student_found = repo.find_by_id(student.get_id())

        assert student_found == None

    def run(self):
        self.test_add()
        self.test_find_by_id()
        self.test_get_all()
        self.test_remove_all()
        self.test_remove_by_id()


t = memory_repo_tests()
t.run()