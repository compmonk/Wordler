import json
import os.path
import unittest
from functools import reduce

from models import WordleTrie, SearchConstraint, Placement


class WordleTrieTests(unittest.TestCase):
    def test_01_initialize_wordle_trie(self):
        # Arrange and Act
        wordle_trie = WordleTrie([])

        # Assert
        self.assertEqual(wordle_trie.value, {}, "")

    def test_02_letters_are_added(self):
        # Arrange and Act
        words = [
            "ROUTE",
            "ROUSH",
        ]
        letters = reduce(lambda l, w: l + list(w), words, [])
        wordle_trie = WordleTrie(words)

        # Assert
        for letter in letters:
            self.assertIn(letter, wordle_trie, "{0} is not added to the Trie".format(letter))

    def test_03_letters_and_position_validation(self):
        # Arrange and Act
        words = [
            "ROUTE",
            "ROUSH"
        ]
        expected = {
            "R": {0: ["ROUTE", "ROUSH"]},
            "O": {1: ["ROUTE", "ROUSH"]},
            "U": {2: ["ROUTE", "ROUSH"]},
            "T": {3: ["ROUTE"]},
            "E": {4: ["ROUTE"]},
            "S": {3: ["ROUSH"]},
            "H": {4: ["ROUSH"]},
        }
        wordle_trie = WordleTrie(words)

        # Assert
        self.assertEqual(wordle_trie.value, expected, "Letters and position are incorrect")

    def test_04_to_json_returns_valid_json(self):
        # Arrange
        words = [
            "ROUTE",
            "ROUSH"
        ]
        expected = json.dumps({
            "R": {0: ["ROUTE", "ROUSH"]},
            "O": {1: ["ROUTE", "ROUSH"]},
            "U": {2: ["ROUTE", "ROUSH"]},
            "T": {3: ["ROUTE"]},
            "E": {4: ["ROUTE"]},
            "S": {3: ["ROUSH"]},
            "H": {4: ["ROUSH"]},
        }, indent=2, sort_keys=True)
        wordle_trie = WordleTrie(words)

        # Act and Assert
        self.assertEqual(wordle_trie.to_json(), expected, "JSON string invalid")

    def test_05_to_json_stores_file_at_path(self):
        # Arrange
        words = [
            "ROUTE",
            "ROUSH"
        ]
        expected = json.dumps({
            "R": {0: ["ROUTE", "ROUSH"]},
            "O": {1: ["ROUTE", "ROUSH"]},
            "U": {2: ["ROUTE", "ROUSH"]},
            "T": {3: ["ROUTE"]},
            "E": {4: ["ROUTE"]},
            "S": {3: ["ROUSH"]},
            "H": {4: ["ROUSH"]},
        }, indent=2, sort_keys=True)
        file_path = "../test_case.json"
        wordle_trie = WordleTrie(words)

        # Act
        wordle_trie.to_json(file_path)

        # Assert
        self.assertTrue(os.path.exists(file_path), "JSON file not created")
        with open(file_path) as json_file:
            self.assertEqual(json_file.read(), expected, "JSON is not valid")

    def test_06_search_possible_word_1(self):
        # Arrange
        words = [
            "ROUTE",
            "ROUSH",
            "BRUSH"
        ]
        wordle_trie = WordleTrie(words)
        search_constraints = [SearchConstraint("R", 0, Placement.PRESENT), SearchConstraint("U", 2, Placement.PLACED)]
        expected = {"BRUSH"}

        # Act
        results = wordle_trie.search(search_constraints)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_07_search_possible_word_2(self):
        # Arrange
        words = [
            "ROUTE",
            "ROUSH",
            "BRUSH",
            "CRUSH"
        ]
        wordle_trie = WordleTrie(words)
        search_constraints = [SearchConstraint("R", 0, Placement.PRESENT), SearchConstraint("U", 2, Placement.PLACED)]
        expected = {"BRUSH", "CRUSH"}

        # Act
        results = wordle_trie.search(search_constraints)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_08_search_possible_word_3(self):
        # Arrange
        words = [
            "ROUTE",
            "ROUSH",
            "BRUSH",
            "CRUSH"
        ]
        wordle_trie = WordleTrie(words)
        search_constraints = [
            SearchConstraint("R", 0, Placement.ABSENT),
            SearchConstraint("U", 2, Placement.PLACED)
        ]
        expected = set()

        # Act
        results = wordle_trie.search(search_constraints)

        # Assert
        self.assertEqual(results, expected, "Results are incorrect")

    def test_09_search_possible_word_5(self):
        # Arrange
        words = [
            "BATCH",
            "HATCH",
            "MATCH",
            "WATCH",
            "BRUSH",
            "BLUSH",
            "BLACK"
        ]
        wordle_trie = WordleTrie(words)
        search_constraints = [
            SearchConstraint("L", 0, Placement.PRESENT),
            SearchConstraint("U", 1, Placement.PRESENT),
            SearchConstraint("Q", 2, Placement.ABSENT),
            SearchConstraint("M", 3, Placement.ABSENT),
            SearchConstraint("H", 4, Placement.PLACED),
        ]
        expected = {"BLUSH"}

        # Act
        results = wordle_trie.search(search_constraints)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))

    def test_10_search_possible_word_6(self):
        # Arrange
        words = [
            "BATCH",
            "HATCH",
            "MATCH",
            "WATCH",
            "BRUSH",
            "BLUSH",
            "BLACK"
        ]
        wordle_trie = WordleTrie(words)
        search_constraints = [
            SearchConstraint("L", 0, Placement.ABSENT),
            SearchConstraint("A", 1, Placement.ABSENT),
            SearchConstraint("S", 2, Placement.PRESENT),
            SearchConstraint("T", 3, Placement.ABSENT),
            SearchConstraint("E", 4, Placement.ABSENT),
        ]
        expected = {"BRUSH"}

        # Act
        results = wordle_trie.search(search_constraints)

        # Assert
        for word in expected:
            self.assertIn(word, results, "Possible word {0} not present in results".format(word))


if __name__ == '__main__':
    unittest.main()
