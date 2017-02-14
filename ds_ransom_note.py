from collections import defaultdict

def ransom_note(magazine, rasom):
    '''input: 6 4
              give me one grand today night
              give one grand today
       output: Yes
    '''
    hashtable = defaultdict(int)
    for word in magazine:
        hashtable[word.lower()] += 1
        
    for word in ransom:
        if hashtable.get(word.lower()) is None:
            return
        else:
            hashtable[word] -= 1
            if hashtable[word] < 0:
                return
    return "Yes"

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"
