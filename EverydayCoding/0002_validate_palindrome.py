from BenchmarkUtil import benchmark_util
NO_OF_SOLUTION = 2


def solution_01(s):
    return s.lower() == s[::-1].lower()


def solution_02(s):
    revs_str = ""
    for c in s:
        revs_str = c + revs_str

    return revs_str.lower() == s.lower()


tests = ["abcdef", "racecar", "This is not", "123454321", "Uppnppu", "LLLLLlllllOOOOOoooooPPPPppppOOOOOooOoOLlLlLlLLLL"]
results = [False, True, False, True, True, True]

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

