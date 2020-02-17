from BenchmarkUtil import benchmark_util
"""Given an integer num, write a method to determine if it is a power of 3.
"""
NO_OF_SOLUTION = 1


def solution_01(n):
    for idx in range(2, int(n/2)):
        if pow(idx, 3) == n:
            return True
        if pow(idx, 3) > n:
            return False
    return False


# def solution_02(n):
#     from math import log
#     if n < 1:
#         return False
#     temp = round(log(n, 3))
#     return n == 3 ** temp


tests = [4, 27, 13, 70097608839168, 700979238322934]
results = [False, True, False, True, False]

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

