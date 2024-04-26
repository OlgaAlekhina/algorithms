def square_digits(n):
    if n == 0:
        return 0
    str_n = []
    sum = ''
    while n != 0:
        str_n.append(n % 10)
        n = n // 10
    sqr_dig = [str(i ** 2) for i in str_n][::-1]
    for i in sqr_dig:
        sum += i

    return int(sum)


print(square_digits(3212))
        
    
    