from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Lista de miembros iniciales con IDs FIJOS
        self._members = [
    {
        "id": 1,
        "first_name": "Tommy",
        "last_name": self.last_name,
        "age": 23,
        "lucky_numbers": [34, 2, 7]
    },
    {
        "id": 2,
        "first_name": "Jane",
        "last_name": self.last_name,
        "age": 35,
        "lucky_numbers": [10, 14, 3],
    },
    {
        "id": 3,
        "first_name": "Jimmy",
        "last_name": self.last_name,
        "age": 5,
        "lucky_numbers": [1],
    }
]


    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" not in member:
            member["id"] = self._generateId()
        if "last_name" not in member:
            member["last_name"] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[i]
                return {"done": True}
        return {"done": False}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        return self._members
