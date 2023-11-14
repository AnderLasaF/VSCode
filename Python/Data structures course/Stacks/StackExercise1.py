#Exercise1: Write a function in python that can reverse a string using stack data structure. 
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"
#RETHINK ON HOW COULD THE CODE BE IMPROVED

from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
    def reverse_string(self,str):
        count = 0
        str_reversed=""
        while count < len(str):
            s.push(str[count])
            count+=1
        
        count2 = 0
        while count2 < len(str):
            str_reversed=str_reversed+s.pop()
            count2+=1

        print(str," original string")
        print(str_reversed," reversed string")

str="We will conquere COVID-19"
s = Stack()
s.reverse_string(str)