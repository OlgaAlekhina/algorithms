from collections import defaultdict


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Set:
    def has_vertical(self, arr):
        vert = None
        dot_dict = defaultdict(list)
        for dot in arr:
            dot_dict[dot.y].append(dot.x)
        for val in dot_dict.values():
            if len(val) % 2 != 0:
                return False
            val.sort()
            val_vert = (val[0] + val[-1]) / 2
            if vert is None:
                vert = val_vert
            else:
                if val_vert != vert:
                    return False
            i, j = 1, len(val) - 2
            while i < j:
                val_vert = (val[i] + val[j]) / 2
                if val_vert != vert:
                    return False
                i += 1
                j -= 2

        return True


d1 = Dot(4, 4)
d2 = Dot(6, 4)
d3 = Dot(3, 3)
d4 = Dot(7, 3)
d5 = Dot(1, 2)
d6 = Dot(2, 2)
d7 = Dot(8, 2)
d8 = Dot(9, 2)
d9 = Dot(4, 2)
d10 = Dot(6, 2)
d11 = Dot(4, 4)
d12 = Dot(4, 4)

s = Set()
print(s.has_vertical([d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]))

# Дан массив точек с целочисленными координатами (x, y). Определить, существует ли вертикальная прямая, делящая точки на 2 симметричных относительно этой
# прямой множества. Note: Для удобства точку можно представлять не как массив [x, y], а как объект {x, y}