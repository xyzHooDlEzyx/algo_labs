class JackieWillBeCaught(Exception):
    def __init__(self, message='Jackie does not have enough time to eat bananas'):
        self.message = message
        super().__init__(self.message)


def min_eating_speed(piles, h):
    if h < len(piles):
        raise JackieWillBeCaught

    def possible(k):
        return sum((pile - 1) // k + 1 for pile in piles) <= h

    minimum, maximum = 1, max(piles)

    while maximum > minimum:
        middle = (minimum + maximum) // 2
        if possible(middle):
            maximum = middle
        else:
            minimum = middle + 1
    return minimum

