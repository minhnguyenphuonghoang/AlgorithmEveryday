from BenchmarkUtil import benchmark_util
"""Merge Intervals
This is a classic question that is used a lot in technical interviews, 
frequently in the form of a calendar or meeting management scenario. 
We'll also assume the same application as it's easier to visualize.

Image credit to https://algorithmsandme.com

Suppose we're given a few arrays, 
like [1, 4], [2, 5], [7, 10], [12, 16].
Each array within it represents a start time and end time of a meeting. 
So an array "time range" of [1, 4] would mean that the event starts at 1 and ends at 4.

Now, what if we wanted to merge any overlapping meetings?
If one meeting runs into the time of another, we'll want to combine them into one. 
As such, [1, 4] and [2, 5] would be combined into [1, 5].

For the above example, 
we would want to return [1, 5], [7, 10], [12, 16]. Can you write a method that will do this?
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

