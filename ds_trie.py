class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self.is_word = False
        self.children = {}
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode('')
        
    def add(self, name):
        node = self.root
        
        for letter in name:
            if letter in node.children:
                node = node.children[letter]
            else:
                node.children[letter] = TrieNode(letter)
                node = node.children[letter]
                
        node.is_word = True
        
    def dfs(node, ):
        if node.is_word:
            
        
    def find(self, partial):
        node = self.root
        
        for letter in partial:
            if letter in node.children:
                node = node.children[letter]
            else: 
                return []    
        
        words = []
        word = partial
        
        while node.children:
            if node.children
        
trie = Trie()

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        trie.add(contact)
    if op == 'find':
        words = trie.find(contact)
        print(len(words))
    
    
