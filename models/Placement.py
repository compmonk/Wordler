from enum import Enum


class Placement(Enum):
    PLACED = "placed"
    PRESENT = "present"
    ABSENT = "absent"

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

    def __eq__(self, other):
        if isinstance(other, Placement):
            return self.value == other.value
        else:
            return self == Placement(other)

    def __hash__(self):
        return hash(self.value)

    @classmethod
    def list(cls):
        return list(map(lambda x: x.value, cls))
