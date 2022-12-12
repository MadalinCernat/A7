import json
import ui
from student import *
from repositories.memory_repository import *
from repositories.textfile_repository import *
from students_service import *


class ui:
    def main(self):
        f = open("settings.json", "r")
        settings = json.load(f)
        f.close()

        repoType = settings["RepositoryType"].lower()
        repository = BaseRepository()

        if repoType == "memory":
            repository = MemoryRepository()
        elif repoType == "textfile":
            file_name = settings["FileName"]
            repository = TextFileRepository(file_name)
        
        service = StudentsService(repository)
        deleted_students = 1

        while True:
            self.print_menu()
            option = int(input())
            
            if option == 1:
                student = self.read_student()
                try:
                    service.add_student(student)
                except ValueError as e:
                    print(e)
            elif option == 2:
                students = service.get_all()
                for stud in students:
                    print(stud)
            elif option == 3:
                group = input("Enter group:")
                deleted_students = service.delete_group_of_students(group)
            elif option == 4:
                service.undo(deleted_students)
                deleted_students = 1
            elif option == 5:
                return

    def print_menu(self):
        print("Choose the operation you want to do:")
        print("1. Add a student")
        print("2. Display the list of students")
        print("3. Delete a group of students")
        print("4. Undo")
        print("5. Exit")

    def read_student(self):
        id = input("Student Id: ")
        name = input("Student Name: ")
        group = input("Student Group: ")
        
        student = Student(id, name, group)
        return student

u = ui()
u.main()