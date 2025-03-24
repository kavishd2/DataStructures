#  File: HuffmanCodes.py
#  Student Name: Kavish Dewani
#  Student UT EID: kd28796
# Python Huffman Compression
from PriorityQueue import PriorityQueue
import sys


# Huffman Node Class
class Huffman_Node(object):
    def __init__(self, ch=None, count=0, left=None, right=None):
        self.ch = ch
        self.count = count
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        if self.ch is None:
            ch = "*"
        else:
            ch = self.ch
        return ch + ", " + str(self.count)


# Build Character Frequency Table
# uses dictionary
# characters added in the order they first occur
def build_char_freq_table(inputString):
    table = {}
    for i in inputString:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1
    return table


# Builds the Huffman Tree
# Creates Huffman Nodes, some pointing to others.
# Returns the root node
def build_huffman_tree(inputString):
    # Build the frequency table, a dictionary of character, frequency pairs
    freq_table = build_char_freq_table(inputString)

    # Build a priority queue, a queue of frequency, character pairs
    # Hightest priority is lowest frequency
    # When a tie in frequency, first item added will be removed first
    priorities = PriorityQueue()
    for key in freq_table:
        node = Huffman_Node(ch=key, count=freq_table[key])
        priorities.push(node)

    # Builds internal nodes of huffman tree, connects all nodes
    while priorities.get_size() > 1: # Pushes the parent node whose children are the first two nodes in the queue
        priorities.push(Huffman_Node("None", priorities.queue[0].count + priorities.queue[1].count, priorities.pop(), priorities.pop()))

    # At the end, priority queue is empty
    # Return the root node of the Huffman Tree
    return priorities.pop()


# After Huffman Tree is built, create dictionary of
# characters and code pairs
def get_huffman_codes(node, prefix, codes):
    if (node.left is None and node.right is None):
        codes[node.ch] = prefix
    else:
        get_huffman_codes(node.left, prefix + "0", codes)
        get_huffman_codes(node.right, prefix + "1", codes)
    return codes


# For each character in input file, returns the Huffman Code
# Input file uses <space> to indicate a space
# If character not found, display "No code found"
def process_chars(data, huff_codes): # Uses codes dictionary to output code for inputs. Formats based on if space
    print("Character    Code")
    for i in range(1,len(data)):
        if data[i][0] == "<":
            if " " in huff_codes:
                print(f"             {huff_codes[' ']}")
            else:
                print("             No code found")
        elif data[i][0] in huff_codes:
            print(f"{data[i][0]}            {huff_codes[data[i][0]]}")
        else:
            print(f"{data[i][0]}            No code found")



''' DRIVER CODE '''

# Open input source
# Change debug to false before submitting
debug = False
if debug:
    in_data = open('message.in')
else:
    in_data = sys.stdin

# read message
data = in_data.readlines()
message = data[0].strip()

# Build Huffman Tree and Codes
root = build_huffman_tree(message)
huff_codes = get_huffman_codes(root, "", {})

# display code for each character in input file
process_chars(data, huff_codes)



