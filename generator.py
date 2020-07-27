import random


def generare_password():
    maiuscole = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minuscole = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    simboli = ['!', '#', '$', '&', '/', '(', ')']
    numeri = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caratteri = maiuscoli + minuscoli + simboli + numeri

    password = []

    for i in range(15):
        caratteri_random = random.choice(caratteri)
        password.append(caratteri_random)

    password = "".join(password)
    return password


def run():
    password = generare_password()
    print('La tua nuova password è: ' + password)


if __name__ == '__main__':
    run()
