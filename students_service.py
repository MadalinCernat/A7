from repositories.base_repository import *
from student import Student
class StudentsService:
    def __init__(self, repository: BaseRepository):
        self._repository = repository
        self.add_sample_data_memory()

    def delete_group_of_students(self, group):
        students = self._repository.get_all()
        students = list(filter(lambda x: (x._group == group), students))
        for s in students:
            self._repository.remove_by_id(s.get_id())
        
        # Return number of deleted students
        return len(students)
    
    def add_student(self, student):
        self._repository.add(student)
    
    def search(self, id):
        return self._repository.find_by_id(id)
    
    def remove(self, id):
        self._repository.remove_by_id(id)
    
    def remove_all(self, id):
        self._repository.remove_all()

    def get_all(self):
        return self._repository.get_all()
    
    def undo(self, deleted_students):
        self._repository.undo(deleted_students)

    
    def add_sample_data_memory(self):
        self._repository.add(Student(1, "Student1", "911"))
        self._repository.add(Student(2, "Student2", "911"))
        self._repository.add(Student(3, "Student3", "912"))
        self._repository.add(Student(4, "Student4", "912"))
        self._repository.add(Student(5, "Student5", "912"))
        self._repository.add(Student(6, "Student6", "914"))
        self._repository.add(Student(7, "Student7", "914"))