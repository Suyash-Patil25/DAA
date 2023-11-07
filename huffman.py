#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self,left=None,right=None,value=None,frequency=None):
        self.left = left
        self.right = right
        self.value = value
        self.frequency = frequency
    
    def children(self):
        return (self.left,self.right)



class Huffman_Encoding:
    def __init__(self,string):
        self.q = []
        self.string = string
        self.encoding = {}

    def char_frequency(self):
        count = {}
        for char in self.string:
            if char not in count:
                count[char] = 0
            count[char] += 1

        for char,value in count.items():
            node = Node(value=char,frequency=value)
            self.q.append(node)
        self.q.sort(key=lambda x: x.frequency)    

    def build_tree(self):
        while len(self.q) > 1:
            n1 = self.q.pop(0)
            n2 = self.q.pop(0)
            node = Node(left=n1,right=n2,frequency=n1.frequency + n2.frequency)
            self.q.append(node)
            self.q.sort(key = lambda x:x.frequency)

    
    def helper(self,node:Node,binary_str=""):
        if type(node.value) is str:
            self.encoding[node.value] = binary_str
            return
        l,r = node.children()
        self.helper(node.left,binary_str + "0")
        self.helper(node.right,binary_str + "1")
        print(node.frequency)
        return
        

    def huffman_encoding(self):
        root = self.q[0]
        self.helper(root,"")


    def print_encoding(self):
        print(' Char | Huffman code ')
        for char,binary in self.encoding.items():
            print(" %-4r |%12s" % (char,binary))
    
    def encode(self):
        self.char_frequency()
        self.build_tree()
        self.huffman_encoding()
        self.print_encoding()

string = input("Enter string to be encoded: ")
# string = 'AAAAAAABBCCCCCCDDDEEEEEEEEE'
encode = Huffman_Encoding(string)
encode.encode()


# The time complexity for encoding each unique character based on its frequency is O(nlog n).

# Extracting minimum frequency from the priority queue takes place 2*(n-1) times and its complexity is O(log n). Thus the overall complexity is O(nlog n).


# In[2]:


import heapq 
class node: 
    def __init__(self, freq, symbol, left=None, right=None): 
        # frequency of symbol 
        self.freq = freq 
  
        # symbol name (character) 
        self.symbol = symbol 
  
        # node left of current node 
        self.left = left 
  
        # node right of current node 
        self.right = right 
  
        # tree direction (0/1) 
        self.huff = '' 
  
    def __lt__(self, nxt): 
        return self.freq < nxt.freq 
  
  
# utility function to print huffman 
# codes for all symbols in the newly 
# created Huffman tree 
def printNodes(node, val=''): 
  
    # huffman code for current node 
    newVal = val + str(node.huff) 
  
    # if node is not an edge node 
    # then traverse inside it 
    if(node.left): 
        printNodes(node.left, newVal) 
    if(node.right): 
        printNodes(node.right, newVal) 
  
        # if node is edge node then 
        # display its huffman code 
    if(not node.left and not node.right): 
        print(f"{node.symbol} -> {newVal}") 
  
  
# characters for huffman tree 
chars = ['a', 'b', 'c', 'd', 'e'] 
  
# frequency of characters 
freq = [4, 2, 3, 5, 1] 
  
# list containing unused nodes 
nodes = [] 
  
# converting characters and frequencies 
# into huffman tree nodes 
for x in range(len(chars)): 
    heapq.heappush(nodes, node(freq[x], chars[x])) 
  
while len(nodes) > 1: 
  
    # sort all the nodes in ascending order 
    # based on their frequency 
    left = heapq.heappop(nodes) 
    right = heapq.heappop(nodes) 
  
    # assign directional value to these nodes 
    left.huff = 0
    right.huff = 1
  
    # combine the 2 smallest nodes to create 
    # new node as their parent 
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right) 
  
    heapq.heappush(nodes, newNode) 
    
printNodes(nodes[0]) 


# In[ ]:




