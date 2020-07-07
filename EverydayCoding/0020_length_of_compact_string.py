from BenchmarkUtil import benchmark_util
"""Day 53: Validate Symbols
We're provided a string like the following that is inclusive of the following symbols:

parentheses '()'
brackets '[]', and
curly braces '{}'.
Can you write a function that will check if these symbol pairings in the string follow these below conditions?

They are correctly ordered
They contain the correct pairings
They are both of the same kind in a pair
For example, () is valid. (( is not. Similarly, {{[]}} is valid. [[}} is not.
"""
NO_OF_SOLUTION = 1


def solution_01(s):
    hash_map = {}
    for item in s:
        if item in hash_map:
            hash_map[item] += 1
        else:
            hash_map[item] = 1
    return hash_map


tests = ["sstttrrrr", "minhnguyenphuonghoang"]
results = [{'s': 2, 't': 3, 'r': 4},
           {'m': 1, 'i': 1, 'n': 5, 'h': 3, 'g': 3, 'u': 2, 'y': 1, 'e': 1, 'p': 1, 'o': 2, 'a': 1}]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result {}, expecting {}".format("solution_0{}".format(sln_idx), result, results[i])

