import random

def guess_the_number():
    # Генерируем случайное число от 0 до 100
    secret_number = random.randint(0, 100)
    attempts = 0
    guessed = False

    print("Я загадал число от 0 до 100. Попробуй отгадать его!")

    while not guessed:
        # Запрашиваем у пользователя ввод числа
        user_guess = int(input("Введите ваше число: "))
        attempts += 1  # Увеличиваем счетчик попыток

        if user_guess < secret_number:
            print("Загаданное число больше.")
        elif user_guess > secret_number:
            print("Загаданное число меньше.")
        else:
            guessed = True
            print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")

# Запускаем игру
guess_the_number()