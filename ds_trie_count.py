class Trie(object):
	def __init__(self):
		self.root = TrieNode()

	def add(self, word):
		node = self.root
		for letter in word:
			if letter in node.children:
				node = node.children[letter]
				node.word_count += 1
			else:
				node.children[letter] = TrieNode()			
				node = node.children[letter]
				node.word_count += 1

	def find(self, partial):
		node = self.root
		count = 0
		for letter in partial:
			if not letter in node.children:
				return 0
			else:
				node = node.children[letter]

		return node.word_count


class TrieNode(object):
	__slots__ = ['word_count', 'children']
	def __init__(self):
		self.word_count = 0	
		self.children = {}

trie = Trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        trie.add(contact)
    if op == 'find':
        print(trie.find(contact))
