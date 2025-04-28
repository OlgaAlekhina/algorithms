def string_int(s: str) -> int:
    nums_dict = {k: v for k, v in zip('0123456789', list(range(10)))}
    res, n = 0, 0
    for char in s[::-1]:
        res += nums_dict[char] * 10 ** n
        n += 1

    return res


print(string_int('0312345'))


# написать функцию, которая переводит строку в число без использования стандатной библиотеки