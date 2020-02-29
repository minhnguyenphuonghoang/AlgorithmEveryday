from BenchmarkUtil import benchmark_util
"""We have an array of length 2 * n (even length) that consists of random integers.

[1, 3, 2, 6, 5, 4]

We are asked to create pairs out of these integers, like such:

[[1, 3], [2, 6], [5, 4]]

How can we divide up the pairs such that the sum of smaller integers in each pair is maximized?

Here's an example input: [3, 4, 2, 5]. The return value is 6 because the maximum sum of pairs is 6 = min(2, 3) + min(4, 5).

Note that negative numbers may also be included.
"""
NO_OF_SOLUTION = 1


def solution_01(s):
    r = s.copy()
    r.sort()
    idx = 0
    total = 0
    while idx < len(r):
        total += r[idx]
        idx += 2
    return total


tests = [[3, 4, 2, 5]]
results = [6]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result {}, expecting {}".format("solution_0{}".format(sln_idx), result, results[i])

