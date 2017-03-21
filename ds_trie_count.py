class Trie(object):
	def __init__(self):
		self.root = TrieNode('')

	def add(self, word):
		node = self.root
		for letter in word:
			if node.children.get(letter):
				node = node.children[letter]
			else:
				node.children[letter] = TrieNode(letter)			
				node = node.children[letter]
		node.is_word = True

	def find(self, partial):
		def dfs(node, count):
			if node.is_word:
				count += 1

			for child in node.children.values():
				count = dfs(child, count)	
			
			return count 

		node = self.root
		count = 0
		for letter in partial:
			if node.children.get(letter):
				node = node.children[letter]
			else:
				return 0

		count += dfs(node, count)		
		
		return count


class TrieNode(object):
	def __init__(self, letter):
		self.letter = letter
		self.is_word = False	
		self.children = {}

trie = Trie()
trie.add('hack')
trie.add('hackerrank')	
print(trie.find('hac'))
print(trie.find('hackerranking'))
