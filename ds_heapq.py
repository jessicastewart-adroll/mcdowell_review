import sys
import heapq

min_heap = []
max_heap = []

def print_median(a_t, min_heap, max_heap):
        # handle the first 2 elements
        if not max_heap and not min_heap:
                heapq.heappush(max_heap, -a_t)
        elif not max_heap:
                if min_heap[0] > a_t:
                        heapq.heappush(max_heap, -a_t)
                else:
                        heapq.heappush(max_heap, -min_heap.pop())
                        heapq.heappush(min_heap, a_t)
        elif not min_heap:
                if -max_heap[0] < a_t:
                        heapq.heappush(min_heap, a_t)
                else:
                        heapq.heappush(min_heap, -max_heap.pop())
                        heapq.heappush(max_heap, -a_t)
        else:
                if a_t < -max_heap[0]:
                        heapq.heappush(max_heap, -a_t)
                else:
                        heapq.heappush(min_heap, a_t)

        # handle additional elements
        max_size = len(max_heap)
        min_size = len(min_heap)
        heapq.heapify(max_heap)
        heapq.heapify(min_heap)

        if max_size == min_size:
                print((-max_heap[0] + min_heap[0])/2)
                return

        while max_size-min_size > 1:
                heapq.heappush(min_heap, -max_heap.pop())
                max_size -= 1
        while min_size-max_size > 1:
                heapq.heappush(max_heap, -min_heap.pop())
                min_size -= 1

        heapq.heapify(max_heap)
        heapq.heapify(min_heap)
        import pdb; pdb.set_trace()
        if max_size > min_size:
                print(float(-max_heap[0]))
        else:
                print(float(min_heap[0]))

n = int(input())
a = []
a_i = 0
for a_i in range(n):
        a_t = int(input())
        a.append(a_t)

        print_median(a_t, min_heap, max_heap)
