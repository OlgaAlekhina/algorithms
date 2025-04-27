from typing import Iterable


def infinity_generator(seq: Iterable):
    seq_len, i = len(seq), 0
    while True:
        yield seq[i]
        i += 1
        if i == seq_len:
            i = 0


for i in infinity_generator([1,2,3]):
    print(i)