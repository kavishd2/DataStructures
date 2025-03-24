# #### Priority Queue

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        results = ""
        for item in self.queue:
            results += item
            return results
    def push(self, item):
        self.queue.append(item)
        self.queue.sort()

    def pop(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            return item
        else:
            raise IndexError("pop from an empty priority queue")

    def is_empty(self):
        return len(self.queue) == 0

    def get_size(self):
        return len(self.queue)

    def print_queue(self):
        for item in self.queue:
            print(item)






