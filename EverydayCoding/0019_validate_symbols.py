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
    hash_map = {
        'parentheses': 0,
        'brackets': 0,
        'curly_braces': 0
    }
    for a_char in s:
        if a_char == "{":
            hash_map['curly_braces'] += 1
        elif a_char == "}":
            hash_map['curly_braces'] -= 1
            if hash_map['curly_braces'] < 0:
                return False
        elif a_char == "(":
            hash_map['parentheses'] += 1
        elif a_char == ")":
            hash_map['parentheses'] -= 1
            if hash_map['parentheses'] < 0:
                return False
        elif a_char == "[":
            hash_map['brackets'] += 1
        else:
            hash_map['brackets'] -= 1
            if hash_map['parentheses'] < 0:
                return False

    for key in hash_map:
        if hash_map[key] < 0:
            return False
    return True


def solution_02(s):
    # Todo:
    #  the above solution is too bad. I must think another way to solve this problem
    return s


tests = ["{{[]}}", "[[}}", "{()}[]()"]
results = [True, False, True]

for i in range(len(tests)):
    for sln_idx in range(1, NO_OF_SOLUTION + 1):
        curr_time = benchmark_util.get_current_time()
        result = eval("solution_0{}".format(sln_idx))(tests[i])
        elapse_time = benchmark_util.get_elapse_time(curr_time)
        # debug:
        print("SOLUTION: {} took {} nanoseconds to finish test.".format(sln_idx, elapse_time))

        assert result == results[i], \
            "Solution {} had wrong result {}, expecting {}".format("solution_0{}".format(sln_idx), result, results[i])

