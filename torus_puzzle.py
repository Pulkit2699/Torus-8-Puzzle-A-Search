# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:25:03 2020

@author: pulkit
"""

def print_succ(state):
    succList = get_succList(state)
    for i in range(len(succList)):
        print(succList[i] , 'h=' , heuristic_succ(succList[i]))
        
    
def get_succList(state):
    succList = []
    for i in state:
        if(state[i] == 0):
            emptyAt = i
    succStates = []
    succ = []
    
    if(emptyAt == 0):
        succ = [1,2,3,6]
    if(emptyAt == 1):
        succ = [0,2,4,7]
    if(emptyAt == 2):
        succ = [0,1,5,8]
    if(emptyAt == 3):
        succ = [0,4,5,6]
    if(emptyAt == 4):
        succ = [1,3,5,7]
    if(emptyAt == 5):
        succ = [2,3,4,8]
    if(emptyAt == 6):
        succ = [0,3,7,8]
    if(emptyAt == 7):
        succ = [1,4,6,8]    
    if(emptyAt == 8):
        succ = [2,5,6,7]
    
    for i in range(len(succ)):
        succStates = state.copy()
        succStates[emptyAt] = succStates[succ[i]]
        succStates[succ[i]] = 0
        succList.append(succStates)
    return succList
    
def heuristic_succ(state):
    heuristic = 0
    for i in range(len(state)):
        if(state[i] == (i + 1) and state[i] != 0):
            heuristic = heuristic + 1  
    return 8 - heuristic

def solve(state):
    #1. Put the start node S on the priority queue, called OPEN
    pq = PriorityQueue()
    list = []
    closed = []
    closedStates = []
    Dict = dict({'state': state, 'h': heuristic_succ(state), 'g': 0, 'parent': None, 'f': heuristic_succ(state)})
    pq.enqueue(Dict)
    #2. If OPEN is empty, exit with failure
    while not pq.is_empty():
        #3. Remove from OPEN and place on CLOSED a node n for which f(n) is minimum
        node = pq.pop() 
        closed.append(node)
        closedStates.append(node['state'])
        #4. If n is a goal node, exit (trace back pointers from n to S)
        if(node['h'] == 0):
            #for i in pq.queue:
             #   print(pq.pop)
            #
            list = printSolution(node)
            list.append(state)
            list.reverse()
            for i in range(len(list)):
                print(list[i], ' h=', heuristic_succ(list[i]), ' moves:', i)
            break;
        succList = get_succList(node['state'])
        
        #5. Expand n, generating all its successors and attach to them pointers back
        #to n. For each successor n' of n
        # succList = get_succList(node['state'])
        for i in range(len(succList)):
            f = node['g'] + 1 + heuristic_succ(succList[i])
            succDict = dict({'state': succList[i], 'h': heuristic_succ(succList[i]), 'g': node['g'] + 1, 'parent': node, 'f': f})
            pq.enqueue(succDict)
            #1. If n' is not already on OPEN or CLOSED estimate h(n'),g(n')=g(n)+
            #c(n,n'), f(n')=g(n')+h(n'), and place it on OPEN.
            #2. If n' is already on OPEN or CLOSED, then check if g(n') is lower for
            #the new version of n'. If so, then:
            
                #1. Redirect pointers backward from n' along path yielding lower g(n').
                #2.Put n' on OPEN.
        #3. If g(n') is not lower for the new version, do nothing.
def printSolution(node):
    list = []
    while(node['parent'] != None):
        list.append(node['state'])
        node = node['parent']
    return list

''' author: hobbes
    source: cs540 canvas
    TODO: complete the enqueue method
'''
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.max_len = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, state_dict):
        """ Items in the priority queue are dictionaries:
             -  'state': the current state of the puzzle
             -      'h': the heuristic value for this state
             - 'parent': a reference to the item containing the parent state
             -      'g': the number of moves to get from the initial state to
                         this state, the "cost" of this state
             -      'f': the total estimated cost of this state, g(n)+h(n)

            For example, an item in the queue might look like this:
             {'state':[1,2,3,4,5,6,7,8,0], 'parent':[1,2,3,4,5,6,7,0,8],
              'h':0, 'g':14, 'f':14}

            Please be careful to use these keys exactly so we can test your
            queue, and so that the pop() method will work correctly.

            TODO: complete this method to handle the case where a state is
                  already present in the priority queue
        """
        in_open = False
        for i in range(len(self.queue)):
            if(state_dict['state'] == self.queue[i]['state']):
                in_open = True
                if(state_dict['g'] < self.queue[i]['g']):
                    self.queue[i]['g'] = state_dict['g']
                    self.queue[i]['f'] = state_dict['f']
                    self.queue[i]['parent'] = state_dict['parent']
            
        
        if not in_open:
            self.queue.append(state_dict)

        # track the maximum queue length
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def requeue(self, from_closed):
        """ Re-queue a dictionary from the closed list (see lecture slide 21)
        """
        self.queue.append(from_closed)

        # track the maximum queue length
        if len(self.queue) > self.max_len:
            self.max_len = len(self.queue)

    def pop(self):
        """ Remove and return the dictionary with the smallest f(n)=g(n)+h(n)
        """
        minf = 0
        for i in range(1, len(self.queue)):
            if self.queue[i]['f'] < self.queue[minf]['f']:
                minf = i
        state = self.queue[minf]
        del self.queue[minf]
        return state

        
    
    
            