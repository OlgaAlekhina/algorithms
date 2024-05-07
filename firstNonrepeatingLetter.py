def first_non_repeating_letter(s):
    char_dict = {}
    for ind, char in enumerate(s.lower()):
        if char in char_dict:
            char_dict[char].append(ind)
        else:
            char_dict[char] = [ind]
    for val in char_dict.values():
        if len(val) == 1:
            return s[val[0]]

    return ''


print(first_non_repeating_letter('hstTSS'))

# Write a function named first_non_repeating_letter† that takes a string input, and returns the first character that is not repeated anywhere in the string.
#
# For example, if given the input 'stress', the function should return 't', since the letter t only occurs once in the string, and occurs first in the string.
#
# As an added challenge, upper- and lowercase letters are considered the same character, but the function should return the correct case for the initial letter. For example, the input 'sTreSS' should return 'T'.
#
# If a string contains all repeating characters, it should return an empty string ("");