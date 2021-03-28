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
    if not isinstance(int_list, list):
        raise TypeError("На вход должен подаваться список")
    result = 0
    for num in int_list:
        if isinstance(num, int) and not isinstance(num, bool):
            if num % 2 != 0:
                result += num
            continue
    return result


if __name__ == '__main__':
    assert odd_sum([1, 2, 4, 3, 7]) == 11

    try:
        int_list = [11.1255, 2.2]
        odd_sum(int_list)

    except TypeError as exc:
        print(exc)
        print("Все элементы списка должны быть целыми числами")
    else:
        print("Решено!")
    finally:
        print("Я выполняюсь в любом случае")