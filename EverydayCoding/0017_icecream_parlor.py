from BenchmarkUtil import benchmark_util
"""Sunny and Johnny like to pool their money and go to the ice cream parlor. 
Johnny never buys the same flavor that Sunny does. 
The only other rule they have is that they spend all of their money.

Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.

For example, they have m=6 to spend and there are flavors costing cost = [1,3,4,5,6].
The two flavors costing 1 and 5 meet the criteria.
Using 1-based indexing, they are at indices 1 and 4.
"""
NO_OF_SOLUTION = 1


def solution_01(s):
    r = s.copy()
    r.sort()
    intervals_merged = []
    idx = 0
    while idx < len(r):
        if idx+1 < len(r) and r[idx][1] >= r[idx+1][0]:
            intervals_merged.append([r[idx][0], r[idx+1][1]])
            idx += 2
        else:
            intervals_merged.append(r[idx])
            idx += 1
    return intervals_merged


def solution_02(s):
    r = s.copy()
    return r


tests = [[[1, 2], [1, 5], [9, 13], [8, 9]], [[1, 4], [2, 5], [7, 10], [12, 16]]]
results = [[[1, 5], [8, 13]], [[1, 5], [7, 10], [12, 16]]]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result {}, expecting {}".format("solution_0{}".format(sln_idx), result, results[i])

