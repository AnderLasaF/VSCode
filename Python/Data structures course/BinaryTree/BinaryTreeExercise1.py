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
        if self.data == val:  #searched value and actual value are the same
            return True

        if val < self.data:  #value might be in the left subtree
            if self.left:    #if there is left node
                return self.left.search(val)   #recursive call to go to the next level
            else:  #if there is no left node, no chance the value is there
                return False

        if val > self.data: #value might be in the right subtree
            if self.right:  #if there is right node
                return self.right.search(val)  #recursive call to go to the next level
            else: #if there is no right node, no chance the value is there
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):  #first root, then the left sub-tree, then the right sub-tree (first their own roots as well)
        elements = []
        elements.append(self.data)  #first is the root

        if self.left:
            elements+= self.left.pre_order_traversal()
        
        if self.right:
            elements+= self.right.pre_order_traversal()
        
        return elements

    def post_order_traversal(self): #print by levels, from left to right, root in the last position
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()
        
        if self.right:
            elements+= self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements
    
    def find_max(self):  #finds maximum value in the binary tree, it has to be the deepest right leaf of the right side

        if self.right:
            return self.right.find_max()

        else:
            return self.data
        
    def find_min(self):  
        if self.left:
            return self.left.find_min()
        
        else:
            return self.data

    def calculate_sum(self):
        sum = 0
        tree_traversal = self.in_order_traversal()  #make use of the in_order_traversal tree, since it's given in a list
        for i in range(len(tree_traversal)):
            sum +=tree_traversal[i]
        return sum


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])  #we always start at the root

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted tree: ",numbers_tree.in_order_traversal())
    print("In order pre traversal gives this sorted tree: ",numbers_tree.pre_order_traversal())
    print("In post order traversal gives this sorted tree: ",numbers_tree.post_order_traversal())
    print("Max of the tree is: ",numbers_tree.find_max())
    print("Min of the tree is: ",numbers_tree.find_min())
    print("The sum of all the elements is: ",numbers_tree.calculate_sum())
    