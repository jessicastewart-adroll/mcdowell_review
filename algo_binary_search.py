def binary_search(a, left, right, to_find):
    while (left <= right):
        mid = left+(right-left)//2
        if a[mid] == to_find:
            return mid
        elif a[mid] < to_find:
            left = mid+1
        else:
            right = mid-1
    
    return -1

def get_flavors(flavors, flavor_count, money):
    i = 0
    while i < flavor_count and flavors[i] <= money: 
        match = binary_search(flavors, i, flavor_count-1, money-flavors[i])
        if match > -1:
            print(i+1, flavors[i])
            print(match+1, flavors[match])
        i+=1  

t = int(input().strip())
for a0 in range(t):
    money = int(input().strip())
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print('new')
    get_flavors(a, n, money)
