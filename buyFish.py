def buy_fish(N, K, price_list):
    result_prices = [price_list[0]]
    days = [0]
    count_days = 1
    for i in range(1, N):
        min_price = price_list[i]
        min_day = i
        L = K if i >= K - 1 else i + 1
        for j in range(L):
            price = price_list[i - j]
            if price < min_price:
                min_price = price
                min_day = i - j
        if min_day == 0:
            result_prices.append(min_price * (i - min_day + 1))
        else:
            result_prices.append(min_price * (i - min_day + 1) + result_prices[min_day - 1])
        if count_days == K and min_day != i:
            count_days = 0
            for i in range(min_day, i):
                days[i] = min_day
                count_days += 1
            count_days += 1
        else:
            if min_day == days[-1]:
                count_days += 1
            else:
                count_days = 1
        days.append(min_day)
    fish_number = []
    for n in range(N):
        fish_number.append(days.count(n))
    return result_prices[-1], fish_number
    
    
print(buy_fish(8, 3, [1,8,4,16,2,5,3,9]))

# Ограничение времени	2 секунды
# Ограничение памяти	256Mb
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt

# Помогите Васе определить, в какие дни и сколько рыбы нужно покупать, чтобы потратить как можно меньше денег.
#
# Формат ввода
# В первой строке вводится два целых числа N и K (1 ≤ N, K ≤ 100 000) — количество дней, в течение которых нужно питаться рыбой, и срок хранения рыбы соответственно.
#
# Во второй строке вводится N чисел, разделенных пробелами: стоимость рыбы в этот день Ci (1 ≤ Ci ≤ 106).
#
# Формат вывода
# В первой строке выведите минимальную сумму, потраченную на рыбу.
#
# Во второй строке выведите N чисел — количество купленных рыб в каждый из дней.
#
# Если правильных ответов несколько — выведите любой из них.
