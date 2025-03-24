#  File: BST_Cipher.py
#  Student Name: Kavish Dewani
#  Student UT EID: kd28796

import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


# The BST Cipher Tree
class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key): # Cleans the key then inserts all characters to tree
        self.root = None
        key = self.clean(key)
        for i in key:
            self.insert(i)

    # Insert one new charater/Node to the BST Cipher tree
    # If the character already exists, don't add it.
    def insert(self, ch):
        node = Node(ch)
        if self.root is None: # Sets the root if tree is empty
            self.root = node
        else: # Otherwise, finds location that character should be and inserts if not there
            current = self.root
            while current is not None:
                if ch == current.ch:
                    return
                if ch < current.ch:
                    if current.left is None:
                        current.left = node
                        current = None
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = node
                        current = None
                    else:
                        current = current.right

    # Encrypts a text message using the BST Tree
    def encrypt(self, message): # Cleans the message then encrypts characters one by one
        message = self.clean(message)
        encrypted = ""
        for i in range(len(message)-1):
            encrypted += self.encrypt_ch(message[i])
            encrypted += "!"
        return encrypted + self.encrypt_ch(message[len(message)-1])

    # Encrypts a single character
    def encrypt_ch(self, ch): # Finds the character in the tree and adds to the encryption while doing so
        current = self.root
        encrypted = ""
        while ch != current.ch:
            if ch < current.ch:
                encrypted += "<"
                current = current.left
            else:
                encrypted += ">"
                current = current.right
        if encrypted == "":
            return "*"
        return encrypted

    # Decrypts an encrypted message using the BST Tree
    def decrypt(self, codes_string): # Decrypts codes one by one
        codes_string = codes_string.split("!")
        decrypted = ""
        for i in codes_string:
            decrypted += self.decrypt_code(i)
        return decrypted

    # Decrypts a single code
    def decrypt_code(self, code): # Traverses through the tree to find the character and if invalid, returns empty string
        current = self.root
        if code == "*":
            return current.ch
        for i in code:
            if current is None:
                return ""
            if i == "<":
                current = current.left
            else:
                current = current.right
        return current.ch


    # Get printed version of BST for debugging
    def BST_print(self):
        if self.root is None:
            return "Empty tree"
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    def clean(self, text):
        cleanText = ""
        for i in range(len(text)):
            if (self.isValidCh(text[i])):
                cleanText += text[i]
        return cleanText

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # read string to be encrypted
    text_message = in_data.readline().strip()

    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
