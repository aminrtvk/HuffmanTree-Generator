# NAME:Aminreza Tavakoli Khorassani
# UCID:30127594
# TUT:05 marcus
# DATE:10 DEC
""" description: this class makes encoding table using a recursive function and go through our tree
and makes codes for the end nodes.
"""
import sys


class EncodingTable:
    """
    A class to represent an Encoding Table made from a Huffman Tree
    Attributes
    ----------
    encode : str
        The dictionary storing for each symbol "char" as binary bit string code "code"
    """

    def __init__(self, tree):
        """
        Constructs an EncodingTable using a HuffmanTree
        :param tree: The HuffmanTree to use to build the EncodingTable dictionary encode
        """
        # Create empty dictionary
        self.encode = {}
        # Launch recursive function to store values into self.encode dictionary
        self.recurse(tree, "")

    # PART 7 (recurse)

    def recurse(self, tree, code):
        #check if every recursive call is based on an object that its bit value isnt none
        if tree.bit is not None:
            if tree.bit == 1:
                code += "1"
            if tree.bit == 0:
                code += "0"
        # base case
        if tree.left is None and tree.right is None:
            self.encode[tree.char] = code
        # recursive cases
        else:
            self.recurse(tree.left, code)
            self.recurse(tree.right, code)
        pass

    # PART 6 (string)
    def __str__(self):
        sr = "" # the string that we are going to return
        sr_list = [] #we make a list to save all the keys from our dictionary
        for char in self.encode.keys():
            sr_list.append(char)
        sr_list.sort()
        # we put all the characters from all list into a big string
        for char in sr_list:
            sr += "{}:{}\n".format(repr(char), self.encode[char])
        # we take out the last character in our string because we dont need \n at the end
        sr = sr[:-1]
        return sr
    def encode_text(self, text):
        """
        Encodes the provided text using the internal encoding dictionary (turns each character symbol into a bit string)
        :param text: The string text to encode
        :return: A bit string "000100" based on the internal encode dictionary
        """
        output_text = ""
        # Loop through characters
        for char in text:
            # If one matches then encode into bitstring
            if char in self.encode:
                output_text += self.encode[char]
            else:
                sys.exit(f"Can't encode symbol {char} as it isn't in the encoding table:\n{self}")
        return output_text
