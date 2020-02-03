from BenchmarkUtil import benchmark_util
"""Here's the definition of an anagram: a word, phrase, or name formed by rearranging the letters of another: 
such as cinema, formed from iceman.

We are given two strings like "cinema" and "iceman" as inputs. Can you write a method isAnagram(str1, str2)
that will return true or false depending on whether the strings are anagrams of each other?
"""
NO_OF_SOLUTION = 2


def solution_01(s):
    str1, str2 = s.split(",")
    str1_arr = list(str1)
    str1_arr.sort()
    str2_arr = list(str2)
    str2_arr.sort()
    return str1_arr == str2_arr


def solution_02(s):
    str1, str2 = s.split(",")
    for a_char in str1:
        if a_char not in str2:
            return False
        str2 = str2.replace(a_char, "", 1)
    return str2 == ""


tests = ["iceman,cinema", "aloha,olaaa", "listen,silent", "blah blah hi,hi blah blal", "characters,racterscha",
         "Mary,Army"]
results = [True, False, True, False, True, False]

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

