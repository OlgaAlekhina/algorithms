from collections import defaultdict


def group_words(word_list):
    word_sorted = []
    for word in word_list:
        word_sorted.append(''.join(sorted(word)))
    word_dict = defaultdict(list)
    for i, word in enumerate(word_sorted):
        word_dict[word].append(i)
    word_groups = []
    for word in word_dict.values():
        for i, val in enumerate(word):
            word[i] = word_list[val]
        word_groups.append(word)

    return word_groups
    

print(group_words(["eat", "tea", "tan", "ate", "nat", "bat"]))

# Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
# Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]
#
# Т.е. сгруппировать слова по "общим буквам".