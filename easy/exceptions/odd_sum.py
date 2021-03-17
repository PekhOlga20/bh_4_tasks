"""
Написать функцию odd_sum, которая принимает список, который может состоять
из различных элементов.
Если все элементы списка целые числа, то функция должна посчитать сумму
нечетных чисел.
Если хотя бы один элемент не является целым числом, то выкинуть ошибку
TypeError с сообщением "Все элементы списка должны быть целыми числами"
Задачу стоит выполнить с помощью одного цикла

Написать блок if __name__ == '__main__', в котором
нужно описать обработку исключения try-except-else-finally
"""

def odd_sum(int_list: list) -> int:
    odd_list =[]
    for item in int_list:
        if isinstance(item, int):
            if isinstance(item, bool):
                continue
            if item % 2 == 0:
                continue
            odd_list += item
    else:
        raise TypeError(f"Все элементы списка должны быть целыми числами")
    return odd_list


if __name__ == '__main__':
    int_list = []
    try:
        print(int)
    except TypeError as exc:
        print (f"Все элементы списка должны быть целыми числами")
    else:
        print(f"Решено!")
    finally:
        print(f"Я выполняюсь в любом случае")