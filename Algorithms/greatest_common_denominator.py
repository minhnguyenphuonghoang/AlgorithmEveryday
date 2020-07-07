def euclid_alg(num1, num2):
    while num2 != 0:
        temp = num1
        num1 = num2
        num2 = temp % num2

    return num1


print(euclid_alg(20, 8))
