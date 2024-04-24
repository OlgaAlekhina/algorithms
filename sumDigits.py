def sum_digits(num):
    sum_dig = 0
    while True:
        sum_dig += num % 10
        num = num // 10
        if num == 0:
            break

    if sum_dig // 10 != 0:
        return sum_digits(sum_dig)

    return sum_dig


print(sum_digits(1238785656906845076968))