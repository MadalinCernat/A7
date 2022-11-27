class StudentsService:
    def __init__(self, repository):
        self._repository = repository

    def delete_group_of_students(self, group):
        students = self._repository.get_all()
        students = list(filter(lambda x: (x._group == group), students))
        for s in students:
            self._repository.remove_by_id(s.get_id())
    