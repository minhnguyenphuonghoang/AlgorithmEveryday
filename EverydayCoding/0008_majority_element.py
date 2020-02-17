from BenchmarkUtil import benchmark_util
"""Suppose we're given an array of numbers like the following:

[4, 2, 4]

Could you find the majority element? A majority is defined as "the greater part, or more than half, of the total.
It is a subset of a set consisting of more than half of the set's elements."

Let's assume that the array length is always at least one, and that there's always a majority element.

In the example above, the majority element would be 4.
"""
NO_OF_SOLUTION = 4


def solution_01(s):
    max_numb = -1
    max_count = -1
    for a_numb in s:
        if s.count(a_numb) > max_count:
            max_count = s.count(a_numb)
            max_numb = a_numb
    if max_count == -1:
        return -1
    else:
        return max_numb


def solution_02(s):
    s_set = set(s)
    max_numb = -1
    max_count = -1
    for a_numb in s_set:
        if s.count(a_numb) > max_count:
            max_count = s.count(a_numb)
            max_numb = a_numb
    if max_count == -1:
        return -1
    else:
        return max_numb


def solution_03(s):
    max_numb = -1
    max_count = -1
    checked_number = []
    for a_numb in s:
        if a_numb in checked_number:
            continue
        if s.count(a_numb) > max_count:
            max_count = s.count(a_numb)
            max_numb = a_numb
        checked_number.append(a_numb)
    if max_count == -1:
        return -1
    else:
        return max_numb


def solution_04(s):
    ocr = {}
    for a_numb in s:
        if a_numb in ocr:
            ocr[a_numb] += 1
        else:
            ocr[a_numb] = 0
    # check for max occur
    max_ocr = -1
    max_numb = -1
    for a_key in ocr:
        if ocr[a_key] > max_ocr:
            max_numb = a_key
            max_ocr = ocr[a_key]
    return max_numb


tests = [[4, 2, 4], [1, 1, 3, 3, 5, 5, 5, 6, 1, 1], [1, 4, 1, 4, 5, 2, 3],
         list(range(1000)) + [3, 300, 300, 50, 50]]
results = [4, 1, 1, 50]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test '{}'.".format(sln_idx, elapse_time, tests[i]))

        assert result == results[i], \
            "Solution {} with test '{}' had wrong result '{}' - expecting '{}'".format("solution_0{}".format(sln_idx),
                                                                                       tests[i], result, results[i])

