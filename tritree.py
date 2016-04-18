__author__ = 'nataLie'


class Node:
    """Class node is a node inside a Class Tree tree"""
    def __init__(self, value):
        self.value = value
        self.leftCh = None
        self.rightCh = None
        self.midCh = None
        self.parent = None
        self.child = None

    def add(self, data):
        """Add a new node with given data"""
        # If Data is same add it to Mid tree.
        if self.value == data:
            if self.midCh:
                return self.midCh.add(data)
            self.midCh = Node(data)
            self.midCh.parent = self
            return True
        elif self.value > data:         # Add to Left
            if self.leftCh:
                return self.leftCh.add(data)
            self.leftCh = Node(data)
            self.leftCh.parent = self
            return True
        else:                           # Add to Right
            if self.rightCh:
                self.rightCh = Node(data)
            self.rightCh=Node(data)
            self.rightCh.parent = self
            return True

    def find(self, data):
        """Find the node with the Data"""
        if self.value == data:  # Got the node with data, nothing more to check. return True.
            return True

        elif self.value > data:
            if self.leftCh:
                return self.leftCh.find(data)
            return False
        else:
            if self.rightCh:
                return self.rightCh.find(data)
            return False

    def update_parent(self, child):
        """Update based on whether I am right or left child of parent"""
        if self.parent.leftCh == self:
            self.parent.leftCh = child
        else:
            self.parent.rightCh = child

    def replace_value_with_rightn(self):
        node = self.rightCh
        while node.leftCh:
            node = node.leftCh

        # update the old parent of child.
        node.parent.leftCh = None
        return node

    def replace_value_with_leftn(self):
        node = self.leftCh
        while node.rightCh:
            node = node.rightCh

        # update the parent and return
        node.parent.rightCh = None
        return node

    def delete(self, data):
        # find replacement.
        if self.value == data:
            if self.midCh is not None:  # If mid is present, Mid will replace the node.
                child = self.midCh
                # updlate right and left to mid.
                child.leftCh = self.leftCh
                child.rightCh = self.rightCh
            elif self.rightCh is not None:
                child = self.replace_value_with_rightn()
            else:
                child = self.replace_value_with_leftn()

            # update child parent to my parent.
            child.parent == self.parent

            # update parent to point to the new child.
            if self.parent is not None:
                self.update_parent(child)
            self.child = child
            return self

        elif self.value > data:   # go left
            return self.leftCh.delete(data)
        else:
            return self.rightCh.delete(data)


class MyTriTree:
    def __init__(self):
        self.root = None

    def add_to_tree(self, data):
        if self.root:
            return self.root.add(data)
        else:
            self.root = Node(data)
            return True

    def find_in_tree(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def delete_in_tree(self, data):
        if self.root is None:
            return False
        else:
            node = self.root.delete(data)
            if self.root == node:
                self.root = node.child
            return node

# bst = MyTriTree()
# # bst.add_to_tree(2)
# # bst.add_to_tree(4)
# # bst.add_to_tree(10)
# # bst.add_to_tree(140)
# # print bst.add_to_tree(5)
# # print bst.add_to_tree(4)
# # print bst.add_to_tree(1)
# # print bst.add_to_tree(6)
# # print bst.find_in_tree(1)
#
# print bst.root
#
#
# # # for i in range(1, 56):
# # #     bst.add_to_tree(i)
# # print (bst.find_in_tree(6))
# # print (bst.delete_in_tree(6))
# # #print(bst.delete_in_tree(56))
# #
#
#
