import unittest

from tests.search_constraint_tests import SearchConstraintTests
from tests.wordle_trie_tests import WordleTrieTests
from tests.wordle_tests import WordleTests

unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite(
    [unittest.TestLoader().loadTestsFromModule(_) for _ in [search_constraint_tests, wordle_trie_tests, wordle_tests]]
))
