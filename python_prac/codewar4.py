"""
Your task is to make a function that can take any non-negative integer as a argument
 and return it with its digits in descending order.
 Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
"""

def sort(any_numb):
    numbers = [x for x in str(any_numb)]
    count = 1
    while count < len(numbers):
        for x in range(len(numbers)-1):
            if numbers[x] < numbers[x+1]:
                numbers[x], numbers[x+1] = numbers[x+1], numbers[x]
        count += 1
    return int(''.join(numbers))

if __name__ == '__main__':
    assert sort(21445) == 54421, '1st example'
    assert sort(145263) == 654321, '2nd example'
    assert sort(1254859723) == 9875543221, '3d example'
    print 'all good!'
