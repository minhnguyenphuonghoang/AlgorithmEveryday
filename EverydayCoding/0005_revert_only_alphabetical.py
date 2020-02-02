from BenchmarkUtil import benchmark_util
"""You are given a string that contains alphabetical characters (a - z, A - Z) and some other characters ($, !, etc.). For example, one input may be:
'sea!$hells3'
Can you reverse only the alphabetical ones?
=> 'sll!$ehaes3'
"""
from re import match
NO_OF_SOLUTION = 1


def solution_01(s):
    pattern = "[a-zA-Z]"
    idx = 0
    jdx = len(s)-1
    new_str = [""]*len(s)
    while idx <= jdx:
        # check if 2 characters are alphabetical to swap
        if match(pattern, s[idx]) and match(pattern, s[jdx]):
            new_str[idx] = s[jdx]
            new_str[jdx] = s[idx]
            idx += 1
            jdx -= 1
        elif not match(pattern, s[idx]):
            new_str[idx] = s[idx]
            idx += 1
        else:
            new_str[jdx] = s[jdx]
            jdx -= 1
    return "".join(new_str)


tests = ["a1b2c3d4", "sea!$hells3", ""]
results = ["d1c2b3a4", "sll!$ehaes3", ""]

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

