from models.Placement import Placement


class SearchConstraint:
    def __init__(self, letter: str = "", index: int = 0, placement: Placement = Placement.ABSENT):
        """
        The Search Constraint built from the information we get from each
        letter of the result of a Wordle game
        :param letter: The letter the result is about
        :param index: The 0 based position the letter was placed at
        :param placement: Whether the letter was placed, present or absent
        """
        self.letter = letter
        self.index = index
        self.placement = placement

    def __str__(self: str):
        """
        String representation of the SearchConstraint
        :return: string version of SearchConstraint
        """
        if self.placement == Placement.PLACED:
            return "{0} is placed at index {1}".format(self.letter, self.index)
        elif self.placement == Placement.PRESENT:
            return "{0} is present but not at index {1}".format(self.letter, self.index)
        elif self.placement == Placement.ABSENT:
            return "{0} is absent".format(self.letter)

    @classmethod
    def from_dict(cls, dicitonary: dict) -> 'SearchConstraint':
        """
        Create a SearchConstrain from a dictionary
        :param dicitonary: A dict holding all the values for SearchConstraint
        :return: A SearchConstraint object
        """

        search_constraint = cls(
            dicitonary.get("letter", ""),
            dicitonary.get("index", 0),
            Placement(dicitonary.get('placement', Placement.ABSENT))
        )

        return search_constraint

    @classmethod
    def from_dicts(cls, dicts: [dict]) -> ['SearchConstraint']:
        """
        Create a list of SearchConstraint from a list of dict
        :param dicts: A list holding dicts which are holding all the values for a SearchConstraint
        :return: A list of SearchConstraint objects
        """

        return [cls.from_dict(_) for _ in dicts]
