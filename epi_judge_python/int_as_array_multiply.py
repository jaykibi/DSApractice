from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = 1
    if num1[0] == 0 or num2[0] == 0:
        return [0]
    if num1[0] < 0 or num2[0] < 0:  # checking if a number is negative
        if num1[0] < 0 and num2[0] < 0:  # if first num of both are negative, set sign to 1, answer will be positive
            sign = 1
        elif num1[0] < 0 or num2[0] < 0:  # if first number of either list is negative switch sign variable to -1
            sign = -1  # need to multiply entire number by sign at the end
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for num1_idx in reversed(range(len(num1))):
        for num2_idx in reversed(range(len(num2))):
            result[num1_idx + num2_idx + 1] += num1[num1_idx] * num2[num2_idx] #
            result[num1_idx + num2_idx] += result[num1_idx + num2_idx + 1] // 10
            result[num1_idx + num2_idx + 1] %= 10

    number_start = 0
    if result[0] == 0:
        for idx in range(len(result)):
            if result[idx] == 0:
                number_start += 1
            else:
                break
        result = result[number_start:]
    return [sign * result[0]] + result[1:]


n1 = [1, 3, 1, 4, 1, 2]
n2 = [-1, 3, 1, 3, 3, 3, 2]
print(multiply(n1, n2))
