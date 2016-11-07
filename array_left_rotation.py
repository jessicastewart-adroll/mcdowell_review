
def array_left_rotation(a, n, k):
    '''input: 5 4
              1 2 3 4 5
       output: 5 1 2 3 4
    '''   
    output = []
    move = k%n
    for val in a[move:]:
        output.append(val)
    for val in a[:move]:
        output.append(val)
            
    return output

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
