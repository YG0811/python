# Отримуємо вхідні дані
input_words = input("Введіть список слів, розділених пробілами: ")
letter_to_filter = input("Введіть літеру для фільтрації: ")

# Розділяємо введений рядок на слова
words = input_words.split()

# Видаляємо слова, які починаються на задану літеру
filtered_words = [word for word in words if not word.startswith(letter_to_filter)]

# Формуємо рядок з обробленими словами, розділеними пробілами
output_words = ' '.join(filtered_words)

# Виводимо результат
print("Результат після видалення слів, які починаються на літеру '{}':".format(letter_to_filter))
print(output_words)
