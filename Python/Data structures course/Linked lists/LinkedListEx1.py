class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next   #pointer to the next element

class LinkedList:
    def __init__(self):
        self.head = None  #points to the head of the linked list

    def print(self):
        if self.head is None:   #blank list
            print("Linked list is empty")
            return
        itr = self.head  #iterator with head assigned to it
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next  #increase/move the iterator
        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        node = Node(data, self.head)  #takes data value and inserts it at the beginning of the list, next element is the current head 
        self.head = node #the new head is the actual inserted node

    def insert_at_end(self, data):
        if self.head is None:  #head is blank
            self.head = Node(data, None)  #next element is none
            return

        itr = self.head  #iterator

        while itr.next:  #if itr.next has some value, we are not at the end, when it becomes null, we are at the last element
            itr = itr.next

        itr.next = Node(data, None)  #next of the last element is null, we have to assign it

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                print(itr.next," itr.next")
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node
        #We will iterate the whole structure until we find it, then we have finished.
        if self.head is None:
            return
        
        count = 0
        itr = self.head #we start iterating in the head
        while itr:  #iterate the whole linked list
            if itr.data==data_after:
                self.insert_at(count+1,data_to_insert)
                break
            itr = itr.next
            count+=1
        
        #different approach:
        
        #if self.head.data == data_after:
            #self.head.next=Node(data_to_insert,self.head.next)
            #return
        
        #itr = self.head
        #while itr:
            #if itr.data == data.after:
                #itr.next = Node(data_to_insert, itr.next)
                #break
            
            #itr = itr.next



    def remove_by_value(self, data):
    # Remove first node that contains data
        count=0
        itr = self.head #start with the head as for every linked list
        while itr:  #iterate the whole linked list
            print(itr.data,"itr.data")
            print("count is: ",count)
            if itr.data==data:
                print(itr.data,"itr.data")
                print("count is: ",count)
                self.remove_at(count)
                break
            itr = itr.next
            count+=1
    
    #different approach
        #if self.head is None:
            #return
        
        #if self.head.data == data:
            #self.head = self.head.next
            #return
        
        #itr = self.head
        #while itr.next:
            #if itr.next.data == data:
                #itr.next = itr.next.next
                #break
            #itr = itr.next

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.print()
    ll.remove_by_value("mango")
    ll.print()
    ll.remove_by_value("apple")
    ll.print()
    ll.remove_by_value("grapes")
    ll.print()
