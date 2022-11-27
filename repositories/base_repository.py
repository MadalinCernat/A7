class BaseRepository():
    def add(self, entity):
        raise NotImplementedError

    def find_by_id(self, entity_id):
        raise NotImplementedError

    def remove_by_id(self, entity_id):
        raise NotImplementedError

    def remove_all(self):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def undo(self, times):
        raise NotImplementedError