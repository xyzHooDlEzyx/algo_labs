class KIsGreaterThenSizeOfArr(Exception):
    def __init__(self, message="K is greater then size of input array"):
        self.message = message
        super().__init__(self.message)


def set_pivot(elem, left, right):
    pivot = elem[right]
    i = left - 1
    for j in range(left, right):
        if elem[j] >= pivot:
            i += 1
            elem[i], elem[j] = elem[j], elem[i]
    elem[i + 1], elem[right] = elem[right], elem[i + 1]
    return i + 1


def quick_select(elem, left, right, k):
    if left <= right:
        pivot_idx = set_pivot(elem, left, right)
        if pivot_idx == k:
            return elem[pivot_idx]
        elif pivot_idx < k:
            return quick_select(elem, pivot_idx + 1, right, k)
        else:
            return quick_select(elem, left, pivot_idx - 1, k)


def find_k_or_error(elem, k):
    if k < 1 or k > len(elem):
        raise KIsGreaterThenSizeOfArr()
    return quick_select(elem, 0, len(elem) - 1, k - 1)
