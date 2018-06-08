"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers except
for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


def find_outlier(integers):
    return filter(lambda x: x % 2, integers)[0] if len(filter(lambda x: x % 2, integers)) == 1 else \
                                                            filter(lambda x: x % 2 == 0, integers)[0]


if __name__ == '__main__':
    assert find_outlier([2, 4, 6, 8, 10, 3]) == 3, '1'
    assert find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]) == 11, '2'
    assert find_outlier([160, 3, 1719, 19, 11, 13, -21]) == 160, '3'
    print 'good!!!'
