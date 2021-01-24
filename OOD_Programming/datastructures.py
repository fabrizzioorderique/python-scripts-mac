'''
Generic Data Structure Module

Created By: Piero Orderique
Date: 24 Jan 2021

Includes:
    Dequeue
    TreeNode
'''
class Dequeue():
    # queue node structure
    class QueueNode():
        def __init__(self, data) -> None:
            self.data = data
            self.next = None
            self.prev = None

    class EmptyDequeueError(Exception):
        pass

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0
    
    def add(self, data):
        ''' pushes the data into queue '''
        t = self.QueueNode(data)
        # if theres a last element, make next point to the new last
        if self.last:
            t.prev = self.last
            self.last.next = t
        self.last = t # now last points to new element pushed

        # if first was None, now its not!
        if not self.first:
            self.first = t

        self.length += 1

    def pop_first(self):
        if not self.first: raise self.EmptyDequeueError
        # else change first to the next!
        self.length -= 1
        n = self.first
        if n == self.last:
            self.first = None
            self.last = None
            return n
        else: # else there are nodes in between
            self.first.next.prev = None
            self.first = self.first.next
            return n 

    def pop_last(self):
        if not self.last: raise self.EmptyDequeueError
        self.length -= 1
        n = self.last
        if n == self.first: 
            self.first = None
            self.last = None
            return n
        else: # else there are nodes in between
            self.last.prev.next = None
            self.last = self.last.prev
            return n

    def __len__(self):
        return self.length