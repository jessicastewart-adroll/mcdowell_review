from collections import defaultdict

def number_needed(a, b):
    '''
    input: 'abc', 'cde'
    output: dcf
    '''
    a_hashtable = defaultdict(int)
    b_hashtable = defaultdict(int)
    number_needed = 0
    
    for letter in a:
        a_hashtable[letter] += 1
        
    for letter in b:
        b_hashtable[letter] += 1    
        
    for key, value in a_hashtable.iteritems():
        if value is not b_hashtable[key]:
            number_needed += abs(value - b_hashtable[key])
            
        if b_hashtable.get(key) is not None:
            del b_hashtable[key]
            
    for key, value in b_hashtable.iteritems():
        if value is not a_hashtable[key]:
            number_needed += abs(value - a_hashtable[key])        
    return number_needed        

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)
