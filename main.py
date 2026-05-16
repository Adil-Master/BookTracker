import json

menu = """1. Добавить книгу
2. Показать все книги
3. Показать среднюю оценку
4. Статистика по авторам
5. Удалить книгу
6. Выход"""

def load_books():
    with open("books.json", 'r', encoding='utf-8') as file:
        return json.loads(file.read())
def save_books(books):
    with open("books.json", 'w', encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False, indent=4)
def main():
    while True:
        print(menu)
        action = input(">")

        if action == "1":
            add_book()

def add_book():
    is_original = True
    books = load_books()
    book = {
        "Автор" : input("Введите автора: "),
        "Название" : input("Введите название:"),
        "Оценка" : input("Введите оценку: "),
        "Дата прочтения" : input("Введите дату прочтения: ")
    }

    for i in books:
        if i['Автор'] == book['Автор'] and i['Название'] == book['Название']:
            print("Отказано, так как данное произведение уже добавлено в список книг.")
            is_original = False

    if is_original:
        books.append(book)
        save_books(books)
if __name__ == "__main__":
    main()