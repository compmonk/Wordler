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

    def test_4_search_constraint_from_dict(self):
        # Arrange
        search_constraint_dict = {
            "letter": "A",
            "index": 4,
            "placement": "present"
        }

        # Act
        search_constraint = self.__class__.search_constraint().from_dict(search_constraint_dict)

        # Act

        self.assertEqual(search_constraint.letter, search_constraint_dict.get("letter"),
                         "letter is not assigned correctly")
        self.assertEqual(search_constraint.index, search_constraint_dict.get("index"),
                         "index is not assigned correctly")
        self.assertEqual(search_constraint.placement, search_constraint_dict.get("placement"),
                         "placement is not assigned correctly")

    def test_5_search_constraints_from_dicts(self):
        # Arrange
        search_constraint_dicts = [
            {
                "letter": "A",
                "index": 0,
                "placement": "present"
            }, {
                "letter": "B",
                "index": 1,
                "placement": "placed"
            }, {
                "letter": "C",
                "index": 2,
                "placement": "present"
            }, {
                "letter": "D",
                "index": 3,
                "placement": "placed"
            }, {
                "letter": "E",
                "index": 4,
                "placement": "absent"
            }
        ]

        # Act
        search_constraints = self.__class__.search_constraint().from_dicts(search_constraint_dicts)

        # Act

        for search_constraint, search_constraint_dict in zip(search_constraints, search_constraint_dicts):
            self.assertEqual(search_constraint.letter, search_constraint_dict.get("letter"),
                             "letter is not assigned correctly")
            self.assertEqual(search_constraint.index, search_constraint_dict.get("index"),
                             "index is not assigned correctly")
            self.assertEqual(search_constraint.placement, search_constraint_dict.get("placement"),
                             "placement is not assigned correctly")


if __name__ == '__main__':
    unittest.main()
