def increment_string(s):
    if s and s[-1].isdigit():
        str_len = len(s)
        count = str_len - 2
        while count >= 0 and s[count].isdigit():
            count -= 1
        num = s[count + 1: str_len]
        increm_num = str(int(num) + 1)
        increm_str = '0' * (len(num) - len(increm_num)) + increm_num
        return s[:count + 1] + increm_str
    return s + '1'

print(increment_string('x'))



# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be considered.