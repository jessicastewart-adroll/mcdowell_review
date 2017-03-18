class TrieNode(object):
  def __init__(self, letter):
    self.letter = letter
    self.is_word = False
    self.children = {}
  
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
    node = self.root
    
    for letter in partial:
      if node.children.get(letter):
        node = node.children[letter]
      else:
        return []
      
    def dfs(node, words, word):  
      if node.is_word:
        words.append(word)
      
      for letter, child in node.children.items():
        dfs(child, words, word+letter)
      
      return words  
      
    words = []
    return dfs(node, words, partial)
        
trie = Trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        trie.add(contact)
    if op == 'find':
        words = trie.find(contact)
        print(len(words))
    
    
