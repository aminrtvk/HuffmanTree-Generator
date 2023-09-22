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
        tree_list = []
        if tree.left is None and tree.right is None:
            if len(tree.char) != 1:
                del tree
                p_tree = tree_list[-1]
                code = code[:-1]
                return p_tree.recurse(p_tree, code)
            if len(tree.char) == 1:
                key = tree.char
                self.encode[key] = code
                p_tree = tree_list[:]
                del tree
                code = code[:-1]
                return self.recurse(p_tree, code)
        if tree.left is not None:
            tree_list.append(tree)
            code += "0"
            tree = tree.left
            return self.recurse(tree, code)
        if tree.right is not None:
            code += "1"
            tree = tree.right
            return self.recurse(tree, code)
        pass

    # PART 6 (string)

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
