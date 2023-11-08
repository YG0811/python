# Отримуємо кількість адрес
n = int(input("Введіть кількість адрес: "))

# Створюємо порожній список для зберігання адрес
addresses = []

# Зчитуємо адреси і додаємо їх до списку
for i in range(n):
    address = input("Введіть адресу: ")
    addresses.append(address)

# Перевіряємо кожну адресу і виводимо лише ті, які мають домен "@example.com"
for address in addresses:
    if "@example.com" not in address:
        continue  # Якщо домен не знайдено, переходимо до наступної адреси
    print(address)
