# def series_maker(n):
#     """
#     time complexity this function is O(n^2)
#     """
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#
#     else:
#         return (series_maker(n - 1) % 10) + (series_maker(n - 1) // 10) + (series_maker(n - 2) % 10) + (
#                 series_maker(n - 2) // 10)


def series_maker(n):
    """
    time complexity this function is O(n)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev_prev = 0
    prev = 1
    value = 0

    for i in range(2, n + 1):
        value = (prev % 10) + (prev // 10) + (prev_prev % 10) + (prev_prev // 10)
        prev, prev_prev = value, prev

    return value


if __name__ == '__main__':
    print(series_maker(1_000_000_000))
