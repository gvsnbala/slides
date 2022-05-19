"""

    * Создайте словарь:
    * {"city": "Москва", "temperature": "20"}
    * Выведите на экран значение ключа city
    * Уменьшите значение "temperature" на 5
    * Выведите на экран весь словарь

    * Проверьте, есть ли в словаре ключ country
    * Выведите значение по-умолчанию "Россия" для ключа country
    * Добавьте в словарь элемент date со значением "27.05.2019"
    * Выведите на экран длину словаря

"""


def main():
    dict_ = {'city': 'Москва', 'temperature': '20'}
    print(dict_['city'])
    dict_['temperature'] = str(int(dict_['temperature']) - 5)
    print(dict_)

    print('country' in dict_.keys())
    print(dict_.get('country', 'Россия'))
    dict_['date'] = '27.05.2019'
    print(len(dict_))


if __name__ == "__main__":
    main()