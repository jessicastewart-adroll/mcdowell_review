'''
use data structure to access data at correct point
http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
'''
class MinIntHeap(object):
        def __init__(self):
                self.size = 0
                self.items = []

        def get_left_child_index(self, parent_index):
                return (2*parent_index) + 1

        def get_right_child_index(self, parent_index):
                return (2*parent_index) + 2

        def get_parent_index(self, child_index):
                return (child_index - 1)/2

        def has_left_child(self, index):
                return self.get_left_child_index(index) < self.size

        def has_right_child(self, index):
                return self.get_right_child_index(index) < self.size

        def has_parent(self, index):
                return self.get_parent_index(index) >= 0

        def left_child(self, index):
                return self.items[self.get_left_child_index(index)]

        def right_child(self, index):
                return self.items[self.get_right_child_index(index)]

        def parent(self, index):
                return self.items[self.get_parent_index(index)]

        def swap(self, index_one, index_two):
                self.items[index_one], self.items[index_two] = self.items[index_two], self.items[index_one]

        def peek(self):
                if self.size == 0:
                        raise Exception("Heap is empty.")
                return self.items[0]

        def poll(self):
                if self.size == 0:
                        raise Exception("Heap is empty.")

                item = self.items[0]
                self.items[0] = self.items[self.size - 1]
                self.size -= 1
                self.heapify_down()
                return item

        def add(self, item):
                self.items.append(item)
                self.size += 1
                self.heapify_up()

        def heapify_up(self):
                index = self.size - 1
                while self.has_parent(index) and self.parent(index) > self.items[index]:
                        self.swap(self.get_parent_index(index), index)
                        index = self.get_parent_index(index)

        def heapify_down(self):
                index = 0
                while self.has_left_child(index):
                        smaller_child_index = self.get_left_child_index(index)
                        if self.has_right_child(index) and self.right_child(index) < self.left_child(index):
                                smaller_child_index = self.get_right_child_index(index)
                        if self.items < self.items[smaller_child_index]:
                                break
                        else:
                                self.swap(index, smaller_child_index)
                        index = smaller_child_index
                        
        def get_upper_midpoint(self):
                upper_index = int(self.size/2)
                return float(self.items[upper_index])

        def get_lower_midpoint(self):
                lower_index = int((self.size/2)-1)
                return float(self.items[lower_index])

        def get_median(self):
                odd = self.size % 2
                if odd:
                    return self.get_upper_midpoint()
                else:
                    return (self.get_lower_midpoint() + self.get_upper_midpoint()) / 2
        
import sys

min_heap_first = MinIntHeap()
min_heap_second = MinIntHeap()

n = int(input())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input())
   a.append(a_t)

   min_heap_first.add(a_t)
   odd = min_heap_first.size % 2
   upper_median = int(min_heap_first.size/2)

   if odd:
        while min_heap_first.size < upper_median:
                min_heap_second.add(min_heap_first.pop())
        print(min_heap_first.peek())
        while min_heap_first.size > 0:
                min_heap_second.add(min_heap_first.pop())

   else:
        while min_heap_first.size < upper_median:
                min_heap_second.add(min_heap_second.pop())
        print(float(min_heap_first.pop() + min_heap_first.pop()) / 2)
        while min_heap_first.size > 0:
                min_heap_second.add(min_heap_first.pop())

