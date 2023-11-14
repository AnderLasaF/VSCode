#Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. 
#That way you can iterate in forward and backward direction.

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None #points to the head of the linked list
        self.tail= None #points to the tail of the linked list

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
            print(self.head,  "head")
            print(itr," head next")
        print(llstr)


    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.tail
        llstr= ''
        while itr:
            llstr += str(itr.data)+ ' --> ' if itr.prev else str(itr.data)
            itr = itr.prev
        print(llstr)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)   

    def insert_at_begining(self, data):  
        if self.head == None:
            node = Node(data, self.head, self.head)  #if no element is in, head and tail are the same
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head, self.tail)  #takes data value and inserts it at the beginning of the list, next element is the current head, previous element is the tail 
            self.head = node #the new head is the actual inserted node

    def insert_at_end(self, data):  #if we insert at the end, the tail is contantly changing
        if self.head is None:  #if we have no elements, head and tail are the same
            self.head = Node(data, None, None)
            self.tail = Node(data, None, None)
            return

        itr = self.head  #iterator variable

        while itr.next: #when itr.next becomes null, we are at the last element, then we don't execute the loop
            itr = itr.next  

        itr.next = Node(data, None, self.tail)  #next of the actual last element, will be the new last element
        self.tail = itr.next  #the new tail is the new last element
    
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 2:  #we reached the previous index to insert the new element
                itr_prev = itr  #we save the previous element
            if count == index - 1:  #we reached the index to insert the new element
                node = Node(data, itr.next, itr_prev)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index): #take into account if we delete the tail
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next  #we move the head to the next element if we delete the first one
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next   #we shift one place, so we skip the one to be deleted
                print(itr.next," itr.next")
                break

            itr = itr.next
            count+=1

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

if __name__ == '__main__':
    ll = DoubleLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_begining("apple")
    ll.print_forward()
    ll.insert_at(2,"lemon")
    ll.print_forward()