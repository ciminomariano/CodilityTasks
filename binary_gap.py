# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def integer_to_list(value):
    digit_string = str(value)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)

    return digit_list


def integer_to_binary(value):
    binary = "{0:b}".format(value)
    return binary


def solution(N):
    # write your code in Python 3.6
    # 1000010001
    list_of_numbers = integer_to_list(N)
    length = len(list_of_numbers)
    count = 0
    binary_gap = 0
    for numbers in range(length):
        if list_of_numbers[numbers] == 0:
            count = count + 1

        else:
            if count > binary_gap:
                binary_gap = count
                count = 0
    print(binary_gap)
    return binary_gap

#Set the integer number To find her binary gap
number = 529
N = integer_to_binary(number)
solution(N)
