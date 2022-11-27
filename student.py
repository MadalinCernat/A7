class Student:
    def __init__(self, id: int, name, group):
        self._id = id
        self._name = name
        self._group = group

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name

    def get_group(self):
        return self._group
    
    def set_group(self, group):
        self._group = group
    
    def get_id(self):
        return self._id
    
    def set_id(self, id):
        self._id = id

    def __str__(self):
        return f"{self._id} {self._name} {self._group}"

    def __eq__(self, __o: object) -> bool:
        if self._id == __o._id and self._name == __o._name and self._group == __o._group:
            return True
        return False