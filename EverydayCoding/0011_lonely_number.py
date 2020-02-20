from BenchmarkUtil import benchmark_util
"""In a given array of numbers, one element will show up once and the others will each show up twice.
Can you find the number that only appears once in O(n) linear time?
Bonus points if you can do it in O(1) space as well.
"""
NO_OF_SOLUTION = 2


def solution_01(s):
    occurrence = {}
    for number in s:
        if number not in occurrence:
            occurrence[number] = 1
        else:
            occurrence[number] += 1

    for number in occurrence:
        if occurrence[number] == 1:
            return number
    
    return None


def solution_02(s):
    if not s:
        return None
    lonely_number = 0 + s[0]
    for j in range(1, len(s)):
        lonely_number ^= s[j]
    return lonely_number


tests = [[1, 1, 3, 4, 4], [], list(range(1, 1000))*2 + [999999]]
results = [3, None, 999999]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result '{}' - expecting '{}'".format("solution_0{}".format(sln_idx),
                                                                                       result, results[i])

