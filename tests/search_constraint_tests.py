import unittest

from models import Placement, SearchConstraint


class SearchConstraintTests(unittest.TestCase):
    def setUp(self) -> None:
        self.__class__.search_constraint = SearchConstraint

    def test_1_search_constraint_init(self):
        # Arrange and Act
        search_constraint = self.__class__.search_constraint()

        # Assert
        self.assertEqual(search_constraint.letter, "", "Letter not set correctly")
        self.assertEqual(search_constraint.index, 0, "Index not set correctly")
        self.assertEqual(search_constraint.placement, Placement.ABSENT, "Placement not set correctly")

    def test_2_search_constraint_init_with_default_placement(self):
        # Arrange and Act
        search_constraint = self.__class__.search_constraint("R", 0)

        # Assert
        self.assertEqual(search_constraint.letter, "R", "Letter not set correctly")
        self.assertEqual(search_constraint.index, 0, "Index not set correctly")
        self.assertEqual(search_constraint.placement, Placement.ABSENT, "Placement not set correctly")

    def test_3_search_constraint_init_with_parameters(self):
        # Arrange and Act
        search_constraint = self.__class__.search_constraint("R", 0, Placement.PLACED)

        # Assert
        self.assertEqual(search_constraint.letter, "R", "Letter not set correctly")
        self.assertEqual(search_constraint.index, 0, "Index not set correctly")
        self.assertEqual(search_constraint.placement, Placement.PLACED, "Placement not set correctly")


if __name__ == '__main__':
    unittest.main()
