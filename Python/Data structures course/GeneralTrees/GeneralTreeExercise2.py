#Build a tree using the TreeNode class and modify the print_tree method to take tree level as input. That should print the tree only up to that level

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

    def print_tree(self,print_level):

        if self.get_level()<=print_level:
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)

            if self.children:
                for child in self.children:
                    child.print_tree(print_level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():

    Ind = TreeNode("India")
    Guj = TreeNode("Gujarat")
    Kar = TreeNode("Karnataka")
    Ind.add_child(Guj)
    Ind.add_child(Kar)
    Guj.add_child(TreeNode("Ahmedabad"))
    Guj.add_child(TreeNode("Baroda"))
    Kar.add_child(TreeNode("Bangluru"))
    Kar.add_child(TreeNode("Mysore"))

    US = TreeNode("USA")
    NY = TreeNode("New Yersey")
    Cali = TreeNode("California")
    US.add_child(NY)
    US.add_child(Cali)
    NY.add_child(TreeNode("Princeton"))
    NY.add_child(TreeNode("Trenton"))
    Cali.add_child(TreeNode("San Francisco"))
    Cali.add_child(TreeNode("Mountain View"))
    Cali.add_child(TreeNode("Palo Alto"))

    root = TreeNode("Global")
    root.add_child(Ind)
    root.add_child(US)


    return root


if __name__ == '__main__':
    root_node = build_location_tree()
    root_node.print_tree(0)
    root_node.print_tree(1)