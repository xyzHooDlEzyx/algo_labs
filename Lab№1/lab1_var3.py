class kIsGreaterThenSizeOfArr (Exception):
    def __init__(self, message = 'K is greater then size of input array'):
        self.message = message
        super().__init__(self.message)

def find_k_max(k, arr):
    n = len(arr)
    if k > n or k <= 0:
        raise kIsGreaterThenSizeOfArr
    if n == 0:
        raise ValueError("Array is empty")

    indexed_arr = [(val, idx) for idx, val in enumerate(arr)]

    for i in range(k):
        max_ind = i
        for j in range(i + 1, n):
            if indexed_arr[j][0] > indexed_arr[max_ind][0]:
                    max_ind = j
        indexed_arr[i], indexed_arr[max_ind] = indexed_arr[max_ind], indexed_arr[i]
    return indexed_arr[k-1][0] , indexed_arr[k-1][1]
