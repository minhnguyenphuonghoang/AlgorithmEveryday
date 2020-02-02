from BenchmarkUtil import benchmark_util
"""Can you write a function that takes two arrays as inputs and returns to us their intersection? 
Let's return the intersection in the form of an array.
"""
NO_OF_SOLUTION = 3


def solution_01(kwargs):
    arr1 = kwargs.get("arr1", [])
    arr2 = kwargs.get("arr2", [])
    intersect_arr = []
    for a_number in arr1:
        if a_number in intersect_arr:
            continue
        if a_number in arr2:
            intersect_arr.append(a_number)
    return intersect_arr


def solution_02(kwargs):
    arr1 = kwargs.get("arr1", [])
    arr2 = kwargs.get("arr2", [])
    intersect_arr = []
    if len(arr1) < len(arr2):
        for a_number in arr1:
            if a_number in intersect_arr:
                continue
            if a_number in arr2:
                intersect_arr.append(a_number)
    else:
        for a_number in arr2:
            if a_number in intersect_arr:
                continue
            if a_number in arr1:
                intersect_arr.append(a_number)
    return intersect_arr


def solution_03(kwargs):
    arr1 = kwargs.get("arr1", [])
    arr2 = kwargs.get("arr2", [])
    intersect_list = list(set(arr1) & set(arr2))
    intersect_list.sort()
    return intersect_list


tests = [{"arr1": [1, 2, 3, 4, 5], "arr2": [2, 4]},
         {"arr1": [1, 2, 2, 3, 4, 3, 5, 1], "arr2": [2, 4]},
         {"arr1": range(1000), "arr2": [100, 900, 1000]},
         {"arr1": range(10000), "arr2": range(9000, 9999, 300)}]
results = [[2, 4], [2, 4], [100, 900], [9000, 9300, 9600, 9900]]

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

