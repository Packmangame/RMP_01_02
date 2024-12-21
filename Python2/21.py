import random

def create_deck():
    # Создаем колоду карт
    return ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4

def card_value(card):
    # Определяем стоимость карты
    if card in ['6', '7', '8', '9', '10']:
        return int(card)
    elif card == 'J':
        return 2
    elif card == 'Q':
        return 3
    elif card == 'K':
        return 4
    elif card == 'A':
        return 11

def play_game():
    deck = create_deck()
    random.shuffle(deck)  # Перемешиваем колоду
    score = 0

    print("Добро пожаловать в игру с картами!")
    
    while True:
        user_input = input("Хотите взять карту? (y/n): ").strip().lower()
        
        if user_input == 'n':
            print(f"Вы набрали {score} очков. Спасибо за игру!")
            break
        elif user_input == 'y':
            if not deck:
                print("В колоде больше нет карт!")
                break
            
            card = deck.pop()  # Берем последнюю карту из колоды
            score += card_value(card)  # Прибавляем стоимость карты к очкам
            print(f"Вы взяли карту: {card}. Текущий счет: {score}.")

            if score > 21:
                print(f"Вы проиграли! У вас {score} очков.")
                break
            elif score == 21:
                print("Поздравляю! Вы выиграли с 21 очком!")
                break
        else:
            print("Пожалуйста, введите 'y' или 'n'.")

    print("До свидания!")

# Запускаем игру
play_game()