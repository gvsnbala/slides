"""
    * Создайте функцию get_summ(one, two, delimiter='&'), 
        которая принимает два параметра, приводит их к 
        строке и отдает объединенными через разделитель delimiter

    * Вызовите функцию, передав в нее два аргумента "Learn" и "python", 
        положите результат в переменную и выведите ее значение на экран

    * Сделайте так, чтобы результирующая строка выводилась 
        заглавными буквами

"""


def get_summ(one, two, delimiter='&') -> str:
    return f'{one}{delimiter}{two}'


def get_summ2(one, two, delimiter='&') -> str:
    return f'{one.capitalize()}{delimiter}{two.capitalize()}'


def main():
    lp = get_summ('Learn', 'python')
    print(lp)
    print(get_summ2('Learn', 'python'))


if __name__ == "__main__":
    main()