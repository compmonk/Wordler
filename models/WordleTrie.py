import json
from functools import reduce

from models import SearchConstraint, Placement


class WordleTrie(dict):
    __value = {}

    def __init__(self, words: [str]):
        """
        This is the Wordle Trie which parses the words and stores them in order
        for easy retrieval using `letter` and `position`
        :param words: A list of words which wold be ordered for easy searching
        """
        super().__init__()
        for word in words:
            self.insert_word(word)

    def __str__(self):
        return self.to_json()

    def __repr__(self):
        return str(self.__value)

    def __contains__(self, item):
        return item in self.__value

    @property
    def value(self):
        return self.__value

    def to_json(self, file_path: str or None = None):
        """
        Converts to the Wordle Trie to json.
        Returns as a json string by default or stores at the given
        `file_path` location
        :param file_path: The location to save the Wordle Tries a json
        :return: Returns a json string if file_path is None
        """
        if file_path:
            with open(file_path, "w") as json_file:
                json.dump(self.__value, json_file, indent=2, sort_keys=True)
        return json.dumps(self.__value, indent=2, sort_keys=True)

    def insert_word(self, word: str):
        """
        Inserts a word in the Wordle Trie
        :param word: The word to insert
        :return: None
        """
        for index, letter in enumerate(word):
            if letter not in self.__value:
                self.__value[letter] = {}

            if index not in self.__value[letter]:
                self.__value[letter][index] = []

            if word not in self.__value[letter][index]:
                self.__value[letter][index].append(word)

    def search(self, search_constraints: [SearchConstraint]):
        """
        Search possible words based on a list of `SearchConstraint`
        :param search_constraints: List of SearchConstraint
        :return: A set containing the possible words
        """
        possible_words = []
        impossible_words = []

        for search_constraint in search_constraints:
            if search_constraint.placement == Placement.PLACED:
                possible_words.append(self.__value.get(search_constraint.letter, {}).get(search_constraint.index, []))
            elif search_constraint.placement == Placement.ABSENT:
                impossible_words.extend(self.__value.get(search_constraint.letter, {}).values())
            elif search_constraint.placement == Placement.PRESENT:
                possible_words.append([])
                for i in self.__value.get(search_constraint.letter, {}).keys():
                    if i == search_constraint.index:
                        impossible_words.append(self.__value.get(search_constraint.letter, {}).get(i, []))
                    else:
                        possible_words[-1].extend(self.__value.get(search_constraint.letter, {}).get(i, []))

            # print(search_constraint, possible_words, impossible_words)
            # print(search_constraint, [[len(words) for words in possible_words]], [[len(words) for words in impossible_words]])

        possible_words = reduce(lambda x, y: set(x).intersection(set(y)), possible_words, set(possible_words[0]))
        impossible_words = reduce(lambda x, y: set(x).union(set(y)), impossible_words, set())
        # print(possible_words, impossible_words)
        return possible_words.difference(impossible_words)
