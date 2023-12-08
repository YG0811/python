expenses = []
categories = set()


def add_expense(amount, category, description):
    expense = {'amount': amount, 'category': category, 'description': description}
    expenses.append(expense)
    categories.add(category)


def generate_report():
    if not expenses:
        print("Нет данных для отчета.")
        return
    for expense in expenses:
        print(f"Сумма: {expense['amount']}, Категория: {expense['category']}, Описание: {expense['description']}")


def show_categories():
    if not categories:
        print("Нет доступных категорий.")
        return
    print("Категории:")
    for category in categories:
        print(category)


# Цикл ввода команд
while True:
    print("\nОпции:")
    print("1. Добавить расход")
    print("2. Сгенерировать отчет")
    print("3. Показать категории")
    print("4. Выход")

    command = input("Введите команду (1/2/3/4): ")

    if command == '1':
        try:
            amount = float(input("Введите сумму: "))
            category = input("Введите категорию: ")
            description = input("Введите описание: ")
            add_expense(amount, category, description)
            print("Расход успешно добавлен.")
        except ValueError:
            print("Неверный ввод. Пожалуйста, введите корректную сумму.")
    elif command == '2':
        generate_report()
    elif command == '3':
        show_categories()
    elif command == '4':
        print("Выход из системы управления бюджетом. До свидания!")
        break
    else:
        print("Неверная команда. Пожалуйста, введите корректную команду (1/2/3/4).")

