class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.end_of_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

n = int(input())
trie = Trie()

for _ in range(n):
    parts = input().split()
    operation = parts[0]
    argument = parts[1]
    
    if operation == "insert":
        trie.insert(argument)
    elif operation == "search":
        print(str(trie.search(argument)).lower())
    elif operation == "startsWith":
        print(str(trie.startsWith(argument)).lower())
