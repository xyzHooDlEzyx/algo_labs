import sys
import unittest

from src.heap_based_priority_queue import PriorityQueue

sys.path.append("E:\\projects\\algo_labs")


class PriorityQueueTest(unittest.TestCase):

    def test_adding(self):
        priority_queue = PriorityQueue()
        priority_queue.add(40, 3)
        priority_queue.add(30, 2)
        priority_queue.add(20, 1)
        priority_queue.add(10, 0)

        self.assertEqual(priority_queue.peek(), 10)

    def test_deleting(self):
        priority_queue = PriorityQueue()
        priority_queue.add(40, 3)
        priority_queue.add(30, 2)
        priority_queue.add(20, 1)
        priority_queue.add(10, 0)

        self.assertEqual(priority_queue.delete(), 10)

    def test_empty(self):
        pq = PriorityQueue()

        self.assertEqual(pq.delete(), None)


if __name__ == "__main__":
    unittest.main()
