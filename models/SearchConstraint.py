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
