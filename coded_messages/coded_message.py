def answer(l, t):
    """

    :param l: Non-empty list of positive integers
    :param t: Target positive integer
    :return: Lexicographically smallest list containing smallest start and end indexes that sum to t.
    Returns [-1, -1] if no such list exists.
    """
    if not l or t < 0:
        return [-1, -1]
    start_index = 0
    end_index = len(l)
    for each in l:
        total = 0

        for index in xrange(start_index, end_index):
            total += l[index]
            if total == t:
                return [start_index, index]
            if total > t or index == end_index:
                start_index += 1
                break
    return [-1, -1]


# l = [4, 3, 10, 2, 8]
# t = 12

l = [1, 2, 3, 4]
t = 15
print(answer(l, t))