from BenchmarkUtil import benchmark_util
"""Zeros to the End
Write a method that moves all zeros in an array to its end. 
You should maintain the order of all other elements. Here's an example:

zerosToEnd([1, 0, 2, 0, 4, 0])
// [1, 2, 4, 0, 0, 0]
And another one:

zerosToEnd([1, 0, 2, 0, 4, 0])
// [1, 2, 4, 0, 0, 0]
Fill in the following function signature:

function zerosToEnd(nums) {
  return;
};
Can you do this without instantiating a new array?
"""
NO_OF_SOLUTION = 1


def solution_01(s):
    r = s.copy()
    idx = 0
    end = len(s) - 1
    while idx <= end:
        if r[idx] == 0:
            while r[end] == 0:
                if end == idx:
                    break
                end -= 1
            temp = r[idx]
            r[idx] = r[end]
            r[end] = temp
            end -= 1
        idx += 1
    return r


# def solution_02(s):
#     r = s.copy()
#     return r


tests = [[1, 0, 2, 0, 4, 0], [0, 0, 0] + list(range(1000))]
results = [[1, 4, 2, 0, 0, 0], [999, 998, 997, 996] + list(range(1, 996)) + [0, 0, 0, 0]]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result {}, expecting {}".format("solution_0{}".format(sln_idx), result, results[i])

