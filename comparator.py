from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return "{}: {}".format(name, score)
        
    def comparator(self, a, b):
      print(a, b)
      if a.score == b.score:
        a if a.name > b.name else b
      else:
        a if a.score > b.score else b

inputs = [('allen', 100), ('allen', 90), ('ben', 100), ('ben', 50)]
data = []
for i in inputs:
    name, score = i
    data.append(Player(name, score))
    
data = sorted(data, key=cmp_to_key(Player.comparator))
# for i in data:
#     print(i.name, i.score)
