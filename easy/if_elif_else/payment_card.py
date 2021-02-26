"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Дана строка, необходимо проверить, является ли она номером банковской карты.
(16 цифр), если нет, то вернуть 'Ошибка'
Если да, то вернуть ее же, только оставив первые 4 и последние 4 цифры,
а остальное заменить символами "*"

ПРИМЕРЫ
--------------------------------------------------------------------------------
'1234567891123456' -> '1234********3456'
'123privet123' -> 'Ошибка'
"""


def hide_card_numbers(card_number: str) -> str:
    """Скрывает номер карты, оставляя только первые 4 и последние 4 цифры

    :param card_number: номер карты
    :type card_number: str

    :return: строка с номером карты со звездочками или строка "Ошибка"
    :rtype: str
    """
    result = None
    return result


if __name__ == '__main__':
    string = input('Введите номер платежной карты: ')
    print(f"Результат: {hide_card_numbers(string)}")
