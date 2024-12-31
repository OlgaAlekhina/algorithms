def find_character(k: int) -> str:
    cycle, word = 0, 'a'
    while k > 1:
        for i in range(2**cycle):
            word += chr(ord(word[i]) + 1)
            k -= 1
            if k == 1:
                break
        cycle += 1

    return word[-1]


print(find_character(1))

# Alice and Bob are playing a game. Initially, Alice has a string word = "a".
#
# You are given a positive integer k.
#
# Now Bob will ask Alice to perform the following operation forever:
#
# Generate a new string by changing each character in word to its next character in the English alphabet, and append it to the original word.
# For example, performing the operation on "c" generates "cd" and performing the operation on "zb" generates "zbac".
#
# Return the value of the kth character in word, after enough operations have been done for word to have at least k characters.
#
# Note that the character 'z' can be changed to 'a' in the operation.
#
#
#
# Example 1:
#
# Input: k = 5
#
# Output: "b"
#
# Explanation:
#
# Initially, word = "a". We need to do the operation three times:
#
# Generated string is "b", word becomes "ab".
# Generated string is "bc", word becomes "abbc".
# Generated string is "bccd", word becomes "abbcbccd".
# Example 2:
#
# Input: k = 10
#
# Output: "c"
#
#
#
# Constraints:
#
# 1 <= k <= 500