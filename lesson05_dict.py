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
    cities = {'city': 'Москва', 'temperature': '20'}
    print(cities['city'])
    cities['temperature'] = str(int(cities['temperature']) - 5)
    print(cities)

    print('country' in cities.keys())
    print(cities.get('country', 'Россия'))
    cities['date'] = '27.05.2019'
    print(len(cities))


if __name__ == "__main__":
    main()