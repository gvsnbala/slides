'''
    * Перепишите функцию discounted(price, discount, max_discount=20) 
        из урока про функции так, чтобы она перехватывала исключения, 
        когда переданы некорректные аргументы.
    * Первые два нужно приводить к вещественному числу при помощи float(), 
        а третий - к целому при помощи int() и перехватывать исключения 
        ValueError и TypeError, если приведение типов не сработало
'''


def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)


def main():
    pass


if __name__ == "__main__":
    main()