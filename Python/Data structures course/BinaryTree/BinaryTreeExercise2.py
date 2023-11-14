#Modify the delete method in the class to use max element from left subtree. You will remove lines marked with #! and use max value from left subtree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def delete(self, val):  #we always start comparing with the root, and then with sub-trees
        if val < self.data:  #value < than root value or actual node value
            if self.left:
                self.left = self.left.delete(val)   #recursive call
        elif val > self.data: #value > than root value or actual node value
            if self.right:
                self.right = self.right.delete(val)  #recursive call
        else:   #the value and the node are the same
            if self.left is None and self.right is None:  #we are in a leave node, which we are "deleting", making it None
                return None
            elif self.left is None: #No left child. We return the right child to the parent, "deleting" the actual node by not referencing it anymore
                return self.right
            elif self.right is None: #No right child. We return the left child node to the parent, "deleting" the actual node by not referencing it anymore
                return self.left

            max_val = self.left.find_max()   
            self.data = max_val  #replace the node value with the max in the left sub-tree
            self.left = self.left.delete(max_val)  #"delete" the duplicate node from the left subtree 
            #!min_val = self.right.find_min()
            #!self.data = min_val   #replace the node value with the min in the right sub-tree
            #!self.right = self.right.delete(min_val)

        return self    #return the complete tree without the "deleted" node, only executed once

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(20)
    print("After deleting 20 ",numbers_tree.in_order_traversal()) # this should print [1, 4, 9, 17, 18, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(9)
    print("After deleting 9 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 17, 18, 20, 23, 34]

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    numbers_tree.delete(17)
    print("After deleting 17 ",numbers_tree.in_order_traversal())  # this should print [1, 4, 9, 18, 20, 23, 34]


    