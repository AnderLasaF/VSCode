#Extend tree class so that it takes name and designation in data part of TreeNode class. Extend print_tree function such that it can print either name tree, designation tree or name and designation tree.

class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self,print_mode):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if print_mode=="name":
            #print(prefix + self.name)
            value = self.name
        elif print_mode=="designation":
            #print(prefix + self.designation)
            value = self.designation
        elif print_mode=="both":
            #print(prefix + self.name + ("(" +self.designation+")"))
            value = self.name + " (" +self.designation+")"
        else:
            print("Wrong input argument")
        
        print(prefix + value)

        if self.children:
            for child in self.children:
                child.print_tree(print_mode)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_management_tree():
    

    ChiefTechOff = TreeNode("Chinmay","CTO")  #all the direct children of CTO added
    InfHead = TreeNode("Vishwa","Infrastructure Head")  
    ChiefTechOff.add_child(InfHead) #node, a child of CTO
    ChiefTechOff.add_child(TreeNode("Aamir","Application Head"))  #leaf
    InfHead.add_child(TreeNode("Dhaval","Cloud Manager"))  #leaf
    InfHead.add_child(TreeNode("Abhijit","App Manager"))  #leaf
    
    HrHe = TreeNode("Gels","HR Head")
    HrHe.add_child(TreeNode("Peter","Recruitment Manager"))
    HrHe.add_child(TreeNode("Waqas","Policy Manager"))

    root = TreeNode("Nilupul","CEO")
    root.add_child(ChiefTechOff)
    root.add_child(HrHe)

    return root


"""
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
"""


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name")
    root_node.print_tree("designation")
    root_node.print_tree("both")
