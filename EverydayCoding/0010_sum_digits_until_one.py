from BenchmarkUtil import benchmark_util
"""Given an integer num, write a method to sum all digits until there is one.
"""
NO_OF_SOLUTION = 2


def solution_01(n):
    if n - (n % 10) == 0:
        return n
    else:
        return solution_01(int(n/10) + n % 10)


def solution_02(n):
    while n - (n % 10) != 0:
        n = int(n/10) + n % 10
    return n


def solution_03(n):
    pass


tests = [49, 10, 11, 999, 999999999999999999999, 9999999999999999999999999999999999999999999999999999999999999999]
results = [4, 1, 2, 9, 1, 1]

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

