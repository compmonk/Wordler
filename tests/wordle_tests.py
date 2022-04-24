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

    def test_284(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.PLACED),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT)
        ]
        expected = {"stove"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_285(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PRESENT),

            SearchConstraint("c", 0, Placement.ABSENT),
            SearchConstraint("l", 1, Placement.PRESENT),
            SearchConstraint("o", 2, Placement.PRESENT),
            SearchConstraint("c", 3, Placement.ABSENT),
            SearchConstraint("k", 4, Placement.ABSENT),

            SearchConstraint("w", 0, Placement.PRESENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("u", 2, Placement.ABSENT),
            SearchConstraint("l", 3, Placement.PLACED),
            SearchConstraint("d", 4, Placement.ABSENT),
        ]
        expected = {"lowly"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_286(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.PRESENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.PLACED),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.PLACED),
            SearchConstraint("o", 2, Placement.PLACED),
            SearchConstraint("r", 3, Placement.ABSENT),
            SearchConstraint("t", 4, Placement.PLACED),
        ]
        expected = {"snout"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_287(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.PRESENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.PRESENT),

            SearchConstraint("r", 0, Placement.PRESENT),
            SearchConstraint("o", 1, Placement.PRESENT),
            SearchConstraint("u", 2, Placement.ABSENT),
            SearchConstraint("t", 3, Placement.PRESENT),
            SearchConstraint("e", 4, Placement.PLACED),

            SearchConstraint("p", 0, Placement.PRESENT),
            SearchConstraint("l", 1, Placement.ABSENT),
            SearchConstraint("o", 2, Placement.PLACED),
            SearchConstraint("n", 3, Placement.ABSENT),
            SearchConstraint("k", 4, Placement.ABSENT),

        ]
        expected = {"trope"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_288(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("b", 0, Placement.ABSENT),
            SearchConstraint("u", 1, Placement.ABSENT),
            SearchConstraint("y", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("f", 0, Placement.PLACED),
            SearchConstraint("e", 1, Placement.PLACED),
            SearchConstraint("v", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),
        ]
        expected = {"fewer"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_289(self):
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
        ]
        expected = {"shawl"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_290(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.PRESENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.PRESENT),
            SearchConstraint("a", 2, Placement.PRESENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PLACED),
        ]
        expected = {"natal"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_291(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PRESENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("v", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("d", 2, Placement.ABSENT),
            SearchConstraint("k", 3, Placement.ABSENT),
            SearchConstraint("a", 4, Placement.PLACED),

            SearchConstraint("g", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("m", 2, Placement.PLACED),
            SearchConstraint("p", 3, Placement.ABSENT),
            SearchConstraint("a", 4, Placement.PLACED),
        ]
        expected = {"comma"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_292(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.PRESENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PRESENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("m", 0, Placement.ABSENT),
            SearchConstraint("a", 1, Placement.PRESENT),
            SearchConstraint("c", 2, Placement.ABSENT),
            SearchConstraint("r", 3, Placement.PRESENT),
            SearchConstraint("o", 4, Placement.PRESENT),

            SearchConstraint("b", 0, Placement.ABSENT),
            SearchConstraint("r", 1, Placement.PRESENT),
            SearchConstraint("o", 2, Placement.PRESENT),
            SearchConstraint("a", 3, Placement.PLACED),
            SearchConstraint("d", 4, Placement.ABSENT),
        ]
        expected = {"foray"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_293(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.PRESENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),
        ]
        expected = {"scare"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_294(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.PLACED),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("i", 3, Placement.PLACED),
            SearchConstraint("l", 4, Placement.ABSENT),
        ]
        expected = {"stair"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_295(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PRESENT),
        ]
        expected = {"stair"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_296(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PRESENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),
        ]
        expected = {"squad"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_298(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.PRESENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.PRESENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("p", 0, Placement.ABSENT),
            SearchConstraint("u", 1, Placement.PRESENT),
            SearchConstraint("n", 2, Placement.PRESENT),
            SearchConstraint("c", 3, Placement.PRESENT),
            SearchConstraint("h", 4, Placement.PRESENT),
        ]
        expected = {"chunk"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_299(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.PRESENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.PRESENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("q", 0, Placement.ABSENT),
            SearchConstraint("u", 1, Placement.ABSENT),
            SearchConstraint("i", 2, Placement.PRESENT),
            SearchConstraint("n", 3, Placement.PRESENT),
            SearchConstraint("e", 4, Placement.PLACED),

        ]
        expected = {"mince"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_300(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.PRESENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.PLACED),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("m", 0, Placement.PRESENT),
            SearchConstraint("a", 1, Placement.PRESENT),
            SearchConstraint("k", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),
        ]
        expected = {"shame"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_300(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.PRESENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("p", 0, Placement.ABSENT),
            SearchConstraint("l", 1, Placement.ABSENT),
            SearchConstraint("u", 2, Placement.ABSENT),
            SearchConstraint("c", 3, Placement.PRESENT),
            SearchConstraint("k", 4, Placement.PLACED),
        ]
        expected = {"cheek"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_301(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PRESENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PRESENT),

            SearchConstraint("p", 0, Placement.PRESENT),
            SearchConstraint("l", 1, Placement.PRESENT),
            SearchConstraint("e", 2, Placement.PRESENT),
            SearchConstraint("a", 3, Placement.PRESENT),
            SearchConstraint("d", 4, Placement.ABSENT),
        ]
        expected = {"ample"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_303(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("p", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("k", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("d", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("z", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),
        ]
        expected = {"foyer"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_304(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("p", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("k", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),

            SearchConstraint("d", 0, Placement.ABSENT),
            SearchConstraint("o", 1, Placement.PLACED),
            SearchConstraint("z", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PLACED),
            SearchConstraint("r", 4, Placement.PLACED),
        ]
        expected = {"foyer"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_305(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PRESENT),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.PRESENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.PRESENT),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.ABSENT),

            SearchConstraint("c", 0, Placement.PLACED),
            SearchConstraint("o", 1, Placement.PRESENT),
            SearchConstraint("b", 2, Placement.ABSENT),
            SearchConstraint("r", 3, Placement.PRESENT),
            SearchConstraint("a", 4, Placement.PRESENT),

        ]
        expected = {"cargo"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_306(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PLACED),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.PRESENT),
            SearchConstraint("l", 4, Placement.ABSENT),
        ]
        expected = {"oxide"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_307(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.PRESENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.ABSENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.PRESENT),
            SearchConstraint("a", 2, Placement.PLACED),
            SearchConstraint("i", 3, Placement.ABSENT),
            SearchConstraint("l", 4, Placement.PRESENT),
        ]
        expected = {"plant"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_308(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.PLACED),
            SearchConstraint("t", 1, Placement.ABSENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.ABSENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.ABSENT),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.PRESENT),
            SearchConstraint("l", 4, Placement.PRESENT),
        ]
        expected = {"olive"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_309(self):
        # Arrange
        search_constraints = [
            SearchConstraint("o", 0, Placement.ABSENT),
            SearchConstraint("t", 1, Placement.PRESENT),
            SearchConstraint("h", 2, Placement.ABSENT),
            SearchConstraint("e", 3, Placement.PRESENT),
            SearchConstraint("r", 4, Placement.PRESENT),

            SearchConstraint("s", 0, Placement.ABSENT),
            SearchConstraint("n", 1, Placement.PLACED),
            SearchConstraint("a", 2, Placement.ABSENT),
            SearchConstraint("i", 3, Placement.PRESENT),
            SearchConstraint("l", 4, Placement.ABSENT),
        ]
        expected = {"inert"}

        # Act
        results = self.__class__.wordle_trie.search(search_constraints)
        print(results)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))


if __name__ == '__main__':
    unittest.main()
