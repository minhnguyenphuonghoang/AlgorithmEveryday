from BenchmarkUtil import benchmark_util
"""The setup is the same as Two Sum-- you're given an array of numbers, and a "goal" number.

Write a method to return an array of the indexes of the two elements in the array that sum up to the goal.
If there are no such elements, return an empty array.

The caveat here is that the numbers are guaranteed to be sorted.

So let's say our goal number was 10. Our numbers to sum to it would be 3 and 7, and their indices 1 and 2 respectively.

let arr = [1, 3, 7, 9, 11];
let goal = 10;
twoSum(arr, goal);
// [1, 2]
Is there an efficient way to figure this out?
"""
NO_OF_SOLUTION = 1


def solution_01(s):
    array = s.get('array', [])
    expected_total = s.get('expected_total', -1)
    for idx in range(len(array)):
        for jdx in range(idx+1, len(array)):
            if array[idx] >= expected_total or array[jdx] >= expected_total:
                break
            if array[idx] + array[jdx] == expected_total:
                return [idx+1, jdx+1]
    return None


def solution_02(s):
    # Todo:
    #  the above solution is too bad. I must think another way to solve this problem
    return s


tests = [{'array': [1, 3, 7, 9, 11], 'expected_total': 10}]
results = [[1, 4]]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result {}, expecting {}".format("solution_0{}".format(sln_idx), result, results[i])

