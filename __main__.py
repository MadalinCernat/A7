import json
import ui
from student import *
from repositories.memory_repository import *
from repositories.textfile_repository import *
from students_service import *


def main():
    f = open("settings.json", "r")
    settings = json.load(f)
    f.close()
    repoType = settings["RepositoryType"].lower()
    repository = BaseRepository()

    if repoType == "memory":
        repository = MemoryRepository()
        add_sample_data_memory(repository)
    elif repoType == "textfile":
        file_name = settings["FileName"]
        repository = TextFileRepository(file_name)
    
    students_service = StudentsService(repository)
    deleted_students = 1
    while True:
        ui.print_menu()
        option = int(input())
        
        if option == 1:
            student = ui.read_student()
            try:
                repository.add(student)
            except ValueError as e:
                print(e)
        elif option == 2:
            students = repository.get_all()
            for stud in students:
                print(stud)
        elif option == 3:
            group = input("Enter group:")
            deleted_students = students_service.delete_group_of_students(group)
        elif option == 4:
            repository.undo(deleted_students)
            deleted_students = 1
        elif option == 5:
            return


def add_sample_data_memory(repository: MemoryRepository):
    repository.add(Student(1, "Student1", "911"))
    repository.add(Student(2, "Student2", "911"))
    repository.add(Student(3, "Student3", "912"))
    repository.add(Student(4, "Student4", "912"))
    repository.add(Student(5, "Student5", "912"))
    repository.add(Student(6, "Student6", "914"))
    repository.add(Student(7, "Student7", "914"))


if __name__ == "__main__":
    main()