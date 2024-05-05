import unittest

from src.prefix_tree import PrefixTree


class TestTrie(unittest.TestCase):

    def test_insert_and_find_word(self):
        tree = PrefixTree()
        words = ["apple", "app", "book", "bad", "bear", "bat"]
        for word in words:
            tree.insert(word)
        self.assertIsNotNone(tree.find("apple"))
        self.assertIsNotNone(tree.find("app"))
        self.assertIsNotNone(tree.find("bear"))
        self.assertIsNone(tree.find("banana"))

    def test_prefix_is_not_a_word(self):
        trie = PrefixTree()
        trie.insert("apple")
        self.assertIsNone(trie.find("app"))

    def test_prefix_is_word(self):
        trie = PrefixTree()
        trie.insert("app")
        self.assertTrue(trie.prefix_search("app"))

    def test_prefix_search(self):
        trie = PrefixTree()
        words = ["apple", "app", "book", "bad", "bear", "bat"]
        for word in words:
            trie.insert(word)
        self.assertTrue(trie.prefix_search("app"))
        self.assertTrue(trie.prefix_search("b"))
        self.assertFalse(trie.prefix_search("c"))


if __name__ == "__main__":
    unittest.main()
