# you will be given a string then you wil ask to return a reverse string of the given string
# for example: given string: "abcd" => return string: "dcba"
from BenchmarkUtil import benchmark_util

NO_OF_SOLUTION = 3


def solution_01(str1):
    return str1[::-1]


def solution_02(str1):
    # swap each character
    new_str = ""
    for c in str1:
        new_str = c + new_str
    return new_str


def solution_03(str1):
    from math import ceil
    # swap the first and the last characters
    # create a list of characters contain the new string
    new_str = [''] * len(str1)
    for idx in range(ceil(len(str1) / 2)):
        new_str[idx] = str1[len(str1) - idx - 1]
        new_str[len(str1) - idx - 1] = str1[idx]
    return "".join(new_str)


tests = ["1234", "abcdef", "  1a 2b 3c 4d", ".   w   @  f21(!"]
results = ["4321", "fedcba", "d4 c3 b2 a1  ", "!(12f  @   w   ."]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} milliseconds to finish test '{}'.".format(sln_idx, elapse_time, tests[i]))

        assert result == results[i], \
            "Solution {} with test '{}' had wrong result '{}' - expecting '{}'".format("solution_0{}".format(sln_idx),
                                                                                       tests[i], result, results[i])
