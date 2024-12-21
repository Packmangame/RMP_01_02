def group_characters(input_string):
    # Разделяем строку на символы
    characters = input_string.split()
    
    # Создаем словарь для группировки символов
    grouped = {}
    
    for char in characters:
        if char in grouped:
            grouped[char].append(char)
        else:
            grouped[char] = [char]
    
    # Преобразуем словарь в вложенный список
    nested_list = list(grouped.values())
    
    return nested_list

# Пример использования
input_string = input("Введите строку символов, разделенных пробелами: ")
result = group_characters(input_string)
print(result)