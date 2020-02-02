from BenchmarkUtil import benchmark_util
NO_OF_SOLUTION = 2


def solution_01(s):
    all_words = s.lower().split(" ")
    dupes = []
    for idx in range(len(all_words)-1):
        if all_words[idx] in dupes:
            continue
        for j in range(idx + 1, len(all_words)-1):
            if all_words[idx] == all_words[j]:
                dupes.append(all_words[idx])
                break
    return dupes


def solution_02(s):
    a = [1, 1, 2, 3]
    b = [1, 2, 3]
    all_words = s.lower().split(" ")
    unq_words = set(all_words)
    dupes = list(all_words - unq_words)
    return dupes


tests = ["nothing duplicated in this sentence", "the dog and the cat", "x one one two two three",
         "three times times times"]
results = [[], ["the"], ["one", "two"], ["times"]]

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

