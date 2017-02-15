from functools import cmp_to_key
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return "{}: {}".format(self.name, self.score)
        
    def comparator(a, b):
      if a.score != b.score:
        return b.score - a.score
      else:
        if a.name == b.name:
          return 0
        else:  
          return -1 if a.name < b.name else 1

inputs = [('allen1', 100), ('allen2', 90), ('ben1', 100), ('ben2', 50)]
data = []
for i in inputs:
    name, score = i
    data.append(Player(name, score))

print(data)    
data = sorted(data, key=cmp_to_key(Player.comparator))
# for i in data:
#     print(i.name, i.score)
