#  File: Josephus.py
#  Student Name: Kavish Dewani
#  Student UT EID: kd28796

import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.first = None
        self.last = None

    # Is the list empty
    def is_empty(self):
        return self.first is None

    # Append an item at the end of the list
    def insert(self, data): # Two cases depending on if list is empty or not
        link = Link(data)
        if self.is_empty():
            self.first = link
            self.last = link
        else:
            self.last.next = link
            self.last = link
            link.next = self.first

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data): # Goes through list to find node with value
        if self.is_empty():
            return None
        current = self.first
        while True:
            if current.data == data:
                return current
            if current == self.last:
                return None
            current = current.next

    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data): # Changes links and first and last if relevant
        if self.is_empty():
            return None
        previous = self.last
        current = self.first
        if previous == current and current.data == data: # Case where there's only 1 link
            self.first = None
            self.last = None
        while True:
            if current.data == data:
                previous.next = current.next
                if current == self.first:
                    self.first = current.next
                if current == self.last:
                    self.last = previous
                return current
            if current == self.last:
                return None
            previous = current
            current = current.next

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step): # Iterates to node that needs to be deleted
        for i in range(step-1):
            start = start.next
        return start.data, self.delete(start.data).next

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self): # Prints list from start to end
        if self.is_empty():
            return "[]"
        out = "["
        current = self.first
        while True:
            if current == self.last:
                out += f"{current}]"
                return out
            out += f"{current}, "
            current = current.next


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers): # Continuously inserts nodes to the end of the list
    list = CircularList()
    for i in range(num_soldiers):
        list.insert(i+1)
    return list


# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count): # Keeps deleting and resets the node to start counting from
    delete = my_list.delete_after(my_list.find(start_data), step_count)
    while not my_list.is_empty():
        print(delete[0])
        start = delete[1]
        delete = my_list.delete_after(start, step_count)
    print(delete[0])


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''


def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('josephus.in')
        # in_data = open('autograde/test_cases/input_4.txt')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
