#Write a function in python that checks if paranthesis in the string are balanced or not. 
#Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.

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
        s = Stack()
        while count < len(str):
            s.push(str[count])
            count+=1
        
        count2 = 0
        while count2 < len(str):
            str_reversed=str_reversed+s.pop()
            count2+=1

        print(str," original string")
        print(str_reversed," reversed string")
    
def is_balanced(str):
        balanced = False
        count = 0
        elements = {"[":"]", "(":")", "{":"}"}
        s_left=Stack()
        s_right=Stack()
        par_str_left=["(","{","["]  #possible parenthesis left
        par_str_right=[")","}","]"] #possible paranthesis right
        while count < len(str):
            if str[count] in par_str_left:
                s_left.push(str[count])
            elif str[count] in par_str_right:
                if (s_right.size()>s_left.size()) :  #we already know the string is not balanced
                    return balanced  
                else:  #we keep iterating
                    s_right.push(str[count])
            count+=1

        if s_left.size()!=s_right.size(): #we know the string is not balanced
            return balanced 
        
        else: #we have to check 
            count = s_left.size() #reset the previous counter
            if elements[s_left.peek()] != s_right.peek(): #1st option: antisimetric 1 to 1, we create a new stack and compare the new one with the s_right, if they are equal the string is antisimetric, we use peek otherwise we are getting rid of elements (using pop)
                s_right_new = Stack() 
                for i in range(s_left.size()):  #we create the new stack, which should be exactly the same as s_right if the string is simetric
                    s_right_new.push(elements[s_left.pop()]) 
                for i in range(s_right_new.size()):  #we iterate both stacks
                    if s_right_new.pop() != s_right.pop(): #if any of the elements is different, the string is not balanced
                        return balanced
                    else:  #the elements match, we keep counting
                        count-=1
                if count == 0:  #the string is balanced
                    balanced = True
                
                return balanced

            else: #antisimetric 1 to 1 but not reverse
                for i in range (s_left.size()):
                    if elements[s_left.pop()] == s_right.pop():
                        count-=1
                if count == 0:
                    balanced = True
                
                return balanced


if __name__ == '__main__':
    print(is_balanced("({a+b})"))     #--> True
    print(is_balanced("))((a+b}{"))   #--> False
    print(is_balanced("((a+b))"))     #--> True
    print(is_balanced("))"))          #--> False
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}")) #--> True
    print(is_balanced("(([[{{}}]]))"))

