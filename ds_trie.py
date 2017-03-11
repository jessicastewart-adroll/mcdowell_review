class TrieNode(object):
    def __init__(self, value):
        self.value = value
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode('')
        self.children = {}
        
    def add(self, name):
        pass
    
    def find(self, partial):
        pass

trie = Trie()

n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')

    if op == 'add':
        trie.add(contact)
    if opp == 'find':
        count = trie.find(contact)
        print(count)
