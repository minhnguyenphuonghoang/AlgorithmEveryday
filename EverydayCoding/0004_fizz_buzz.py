from BenchmarkUtil import benchmark_util
"""Fizz Buzz is a classic interview question that apparently many engineering candidates can't solve! Let's cover it today.

We're given a number in the form of an integer n.

Write a function that returns the string representation of all numbers from 1 to n based on the following rules:

If it's a multiple of 3, represent it as "fizz".

If it's a multiple of 5, represent it as "buzz".

If it's a multiple of both 3 and 5, represent it as "fizzbuzz".

If it's neither, just return the number itself.

As such, fizzBuzz(15) would result in '12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz'."""

NO_OF_SOLUTION = 2


def solution_01(n):
    final_str = ""
    for idx in range(1, n+1):
        if idx % 3 != 0 and idx % 5 != 0:
            final_str += str(idx)
            continue
        if idx % 3 == 0:
            final_str += "fizz"
        if idx % 5 == 0:
            final_str += "buzz"
    return final_str


def solution_02(n):
    if n == 1:
        return "1"
    if n % 3 != 0 and n % 5 != 0:
        return solution_02(n-1) + str(n)
    curr_str = ""
    if n % 3 == 0:
        curr_str += "fizz"
    if n % 5 == 0:
        curr_str += "buzz"
    return solution_02(n-1) + curr_str


tests = [2, 4, 15, 100]
results = ["12", "12fizz4", "12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz",
           "12fizz4buzzfizz78fizzbuzz11fizz1314fizzbuzz1617fizz19buzzfizz2223fizzbuzz26fizz2829fizzbuzz3132fizz34buzz" +
           "fizz3738fizzbuzz41fizz4344fizzbuzz4647fizz49buzzfizz5253fizzbuzz56fizz5859fizzbuzz6162fizz64buzzfizz6768" +
           "fizzbuzz71fizz7374fizzbuzz7677fizz79buzzfizz8283fizzbuzz86fizz8889fizzbuzz9192fizz94buzzfizz9798fizzbuzz"]

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

