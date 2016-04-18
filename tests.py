__author__ = 'nataLie'


# pip install coverage

import unittest
import tritree

class TestMyTriTree(unittest.TestCase):

    def setUp(self):
        self.tree = tritree.MyTriTree()

    def test_empty_tree(self):
        empty_tree = None
        self.assertTrue(self.tree.add_to_tree, empty_tree)

   # @parameterized()
    def test_empty_tree(self):
        testu = 2
        empty_tree = None

        test = self.tree.add_to_tree(testu)
        self.assertEqual(True, )

if __name__ == "__main__":
    unittest.main(verbosity=2)