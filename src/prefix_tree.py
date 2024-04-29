class TrieNode:
    def __init__(self, text=""):
        self.text = text
        self.children = dict()
        self.is_end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0 : i + 1]
                current.children[char] = TrieNode(prefix)
            current = current.children[char]
        current.is_end_of_word = True

    def find(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return None
            current = current.children[char]
        if current.is_end_of_word:
            return current

    def prefix_search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
