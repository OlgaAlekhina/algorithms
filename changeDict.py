def change_dict(old_dict: dict) -> dict:
    return {k: v for k, v in zip(old_dict.values(), old_dict.keys())}


print(change_dict({'key1': 1, 'key2': 2, 'key3': 3}))


# написать функцию, которая принимает словарь и возвращает словарь, в котором поменялись местами ключи и значения