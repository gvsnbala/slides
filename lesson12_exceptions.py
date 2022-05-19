'''

Перепишите функцию hello_user() из задания про while, 
чтобы она перехватывала KeyboardInterrupt, писала пользователю 
"Пока!" и завершала работу при помощи оператора break

'''

def hello_user():
    while True:
        try:

            value = input('Скажи что-нибудь: ')
            print(value)

        except KeyboardInterrupt:
            print('\nПока')
            break


def main():
    hello_user()


if __name__ == "__main__":
    main()