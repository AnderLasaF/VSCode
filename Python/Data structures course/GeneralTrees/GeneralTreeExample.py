class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


#Extend the class TreeNode, so that we create a child class that inherits from TreeNode
#We can add extra attributes to a child class other than those inherited by the parent class just like we add any other attribute. 

class TreeNodeExtended(TreeNode):

    def __init__(self,data,value=None):
        super().__init__(data)
        self.value = value  #we added the property value to the TreeNodeExtended class

    def print_tree_extended(self):  #printing is different, so we define a new method for the child class
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data + ' ' + self.value if self.value!=None and self.parent!=None else prefix + self.data + ' ')
        if self.children:
            for child in self.children:
                child.print_tree_extended()

def build_product_tree_extended():

    rootNodeExtended = TreeNodeExtended("CoffeMachines")
    rootNodeExtended.add_child(TreeNodeExtended("Phillips","800"))  #add child method is equal, so we inherit it from the parent class
    rootNodeExtended.add_child(TreeNodeExtended("DeLonghi","650"))
    rootNodeExtended.add_child(TreeNodeExtended("Cecotec","250"))

    rootNodeExtended.print_tree_extended()

#add the value if the node is a children
if __name__ == '__main__':
    build_product_tree()
    build_product_tree_extended()
