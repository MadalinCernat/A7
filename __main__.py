import json
import ui
from student import *
from repositories.memory_repository import *
from repositories.textfile_repository import *
from students_service import *


def main():
    f = open("settings.json", "r")
    settings = json.load(f)
    repoType = settings["RepositoryType"].lower()
    repository = BaseRepository()

    if repoType == "memory":
        repository = MemoryRepository()
    elif repoType == "textfile":
        file_name = settings["FileName"]
        repository = TextFileRepository(file_name)
    
    students_service = StudentsService(repository)
    
    while True:
        ui.print_menu()
        option = int(input())

        if option == 1:
            student = ui.read_student()
            repository.add(student)
        elif option == 2:
            students = repository.get_all()
            for stud in students:
                print(stud)
        elif option == 3:
            group = input("Enter group:")
            students_service.delete_group_of_students(group)
        elif option == 5:
            return

main()