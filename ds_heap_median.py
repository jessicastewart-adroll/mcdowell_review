from collections import deque,Counter
from bisect import insort, bisect_left
from itertools import islice

def RunningMode(seq,N,M):
    """
    Purpose: Find the mode for the points in a sliding window as it 
             is moved from left (beginning of seq) to right (end of seq)
             by one point at a time.
     Inputs:
          seq -- list containing items for which a running mode (in a sliding window) is 
                 to be calculated
            N -- length of sequence                      
            M -- number of items in window (window size) -- must be an integer > 1
     Otputs:
        modes -- list of modes with size M - N + 1
       Note:
         1. The mode is the value that appears most often in a set of data.
         2. In the case of ties it the last of the ties that is taken as the mode (this
            is not by definition).
    """    
    # Load deque with first window of seq 
    d = deque(seq[0:M]) 

    modes = [Counter(d).most_common(1)[0][0]]  # contains mode of first window

    # Now slide the window by one point to the right for each new position (each pass through 
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    for item in islice(seq,M,N):
        old = d.popleft()                      # pop oldest from left
        d.append(item)                         # push newest in from right
        modes.append(Counter(d).most_common(1)[0][0])        
    return modes    

def RunningMedian(seq, M):
    """
     Purpose: Find the median for the points in a sliding window (odd number in size) 
              as it is moved from left to right by one point at a time.
      Inputs:
            seq -- list containing items for which a running median (in a sliding window) 
                   is to be calculated
              M -- number of items in window (window size) -- must be an integer > 1
      Otputs:
         medians -- list of medians with size N - M + 1
       Note:
         1. The median of a finite list of numbers is the "center" value when this list
            is sorted in ascending order. 
         2. If M is an even number the two elements in the window that
            are close to the center are averaged to give the median (this
            is not by definition)
    """   
    seq = iter(seq)
    s = []   
    m = M // 2

    # Set up list s (to be sorted) and load deque with first window of seq
    s = [item for item in islice(seq,M)]    
    d = deque(s)

    # Simple lambda function to handle even/odd window sizes    
    median = lambda : s[m] if bool(M&1) else (s[m-1]+s[m])*0.5

    # Sort it in increasing order and extract the median ("center" of the sorted window)
    s.sort()    
    medians = [median()]   

    # Now slide the window by one point to the right for each new position (each pass through 
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    for item in seq:
        old = d.popleft()          # pop oldest from left
        d.append(item)             # push newest in from right
        del s[bisect_left(s, old)] # locate insertion point and then remove old 
        insort(s, item)            # insert newest such that new sort is not required        
        medians.append(median())  
    return medians

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   a.append(a_t)
   print(float(RunningMedian(a,a_t)[0]))
