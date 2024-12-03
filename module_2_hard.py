import random


def pwd(n):
    key = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                key += str(i) + str(j)
    return f'Ключ: {n} - {key}'


n = random.randint(3, 20) # Вариант рандомного значения ключа
# n = int(input('Введите число от 3 до 20: ')) # Вариант ручного введения ключа
password = pwd(n)
print(password)
