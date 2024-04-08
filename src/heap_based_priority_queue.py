class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.size = 0

    def shift_up(self, idx):
        parent_idx = (idx - 1) // 2
        if idx <= 0:
            return
        elif self.heap[idx] < self.heap[parent_idx]:
            self.swap(idx, parent_idx)
            self.shift_up(parent_idx)

    def shift_down(self, idx):
        largest = idx
        left = idx * 2 + 1
        right = idx * 2 + 2

        if left < self.size and self.heap[left] > self.heap[largest]:
            largest = left
        if right < self.size and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != idx:
            self.swap(idx, largest)
            self.shift_down(largest)

    def peek(self):
        if self.heap:
            return self.heap[0].value
        return None

    def add(self, value, priority):
        node = Node(value, priority)
        self.heap.append(node)
        self.size = len(self.heap)
        self.shift_up(self.size-1)

    def delete(self):
        if not self.heap:
            return None
        self.swap(0, self.size-1)
        value_to_delete = self.heap.pop()
        self.size -= 1
        self.shift_down(0)
        return value_to_delete.value

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


if __name__ == "__main__":
    priority_queue = PriorityQueue()
    priority_queue.add(40, 3)
    priority_queue.add(30, 2)
    priority_queue.add(20, 1)
    priority_queue.add(10, 0)

    print(priority_queue.delete())
    print(priority_queue.peek())

