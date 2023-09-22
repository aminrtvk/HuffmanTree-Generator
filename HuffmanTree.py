# NAME:Aminreza Tavakoli Khorassani
# UCID:30127594
# TUT:05 marcus
# DATE:10 DEC
""" description: we have defined a class consisting five prompts which three of them
are optional , we overwrote some built-in functions (str , rper, lt , eq)
and we have two functions that one of them makes trees and the other one combines two trees
"""
class HuffmanTree:
    """
    A class to represent an Huffman Tree
    Attributes
    ----------
    char : str
        The characters represented by this tree
    count : int
        The count of how many times char occurred in the text
    left : HuffmanTree/None
        The left HuffmanTree below this one
    right : HuffmanTree/None
        The right HuffmanTree below this one
    bit : bool
        The bit symbol used to reach this HuffmanTree (either True/False for 1/0)


    General Structure
                         HuffmanTree (char,count,bit)
                          /    \
                      left    right
                        /        \
                HuffmanTree      HuffmanTree

    Default Structure
                         HuffmanTree (char,count,None)
                          /    \
                      left    right
                        /        \
                     None         None
    """
    # PART1 (constructor)
    def __init__(self, char, count, left=None, right=None, bit=None):
        self.char = char
        self.count = count
        self.left = left
        self.right = right
        self.bit = bit
    # PART2 (order)
    # we are comparing two objects by their counts and if they were equal we compare them by their char letter
    def __lt__(self, other):
        if self.count > other.count:
            return True
        elif self.count < other.count:
            return False
        elif self.count == other.count:
            if self.char > other.char:
                return True
            else:
                return False
    # PART3 (string)
    # making a string that can show objects otherwise we couldnt read them
    def __str__(self):
        return f"({self.char},{self.count},{self.left},{self.right},{self.bit})"
    # PART3 (representation)
    # a recursive function that calls itself
    def __repr__(self):
        return f"HuffmanTree({repr(self.char)},{repr(self.count)},{repr(self.left)},{repr(self.right)},{repr(self.bit)})"

    # PART5 (equality)
    # chechks if a tree is equal to another tree based on the requirements of the assignment description
    def __eq__(self, other):
        if other is None:
            return False
    # if the characters ,left and right values are the same then our trees are equal
        if self.char == other.char and self.left == other.left and self.right == other.right:
            return True
        else:
            return False
# PART1 (make_trees)

# we are making a list of tree objects
def make_trees(dictionary):
    trees_list = []
    for char in dictionary:
        trees_list.append(HuffmanTree(char, dictionary[char]))
    return trees_list

# PART4 (merge)

# merging two trees by adding their characters and their counts also
# assigning trees to left or right based on their value and also assigning a value to
# bit based on being smaller or being bigger


def merge(t1, t2):
    if t1 > t2:
        smaller_tree = t2
        t2.bit = 0
        bigger_tree = t1
        t1.bit = 1
    else:
        smaller_tree = t1
        t1.bit = 0
        bigger_tree = t2
        t2.bit = 1
    char_f = smaller_tree.char + bigger_tree.char
    count_f = smaller_tree.count + bigger_tree.count
    left_f = smaller_tree
    right_f = bigger_tree
    return HuffmanTree(char_f, count_f, left_f, right_f, None)

