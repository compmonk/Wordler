import unittest
from pathlib import Path

from models import WordleTrie, SearchConstraint, Placement


class WordleTests(unittest.TestCase):
    def setUp(self) -> None:
        with open(Path(__file__).resolve().parent.parent / "wordle.txt") as wordle_file:
            self.__class__.wordle_trie = WordleTrie(map(lambda x: x.strip(), wordle_file.readlines()))

    def test_269(self):
        # Arrange
        search_constraints = [
            SearchConstraint("f", 0, Placement.ABSENT),
            SearchConstraint("e", 1, Placement.PLACED),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("s", 3, Placement.PLACED),
            SearchConstraint("t", 4, Placement.PRESENT)
        ]
        expected = {"tease"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_280(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.PRESENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),
        ]
        expected = {"epoch"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_281(self):
        # Arrange
        search_constraints = [
            SearchConstraint("a", 0, Placement.ABSENT),
            SearchConstraint("d", 1, Placement.ABSENT),
            SearchConstraint("i", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("u", 4, Placement.ABSENT),

            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.PRESENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("h", 0, Placement.PRESENT),
            SearchConstraint("y", 1, Placement.PLACED),
            SearchConstraint("m", 2, Placement.PLACED),
            SearchConstraint("n", 3, Placement.PRESENT),
            SearchConstraint("s", 4, Placement.ABSENT),
        ]
        expected = {"nymph"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_282(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.PRESENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("p", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("u", 2, Placement.PLACED),
            SearchConstraint("n", 3, Placement.PLACED),
            SearchConstraint("d", 4, Placement.PLACED),

            SearchConstraint("w", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("u", 2, Placement.PLACED),
            SearchConstraint("n", 3, Placement.PLACED),
            SearchConstraint("d", 4, Placement.PLACED),

            SearchConstraint("b", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("u", 2, Placement.PLACED),
            SearchConstraint("n", 3, Placement.PLACED),
            SearchConstraint("d", 4, Placement.PLACED)
        ]
        expected = {"found"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_283(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.PRESENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PLACED),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("h", 1, Placement.PLACED),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("w", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PLACED)
        ]
        expected = {"shall"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))


if __name__ == '__main__':
    unittest.main()
