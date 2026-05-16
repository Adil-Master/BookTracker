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
        elif action == "2":
            ShowBooks()
        elif action == "3":
            arithmetic_mean()
        elif action == "4":
            authors_count()
        elif action == "5":
            delete()
        elif action == "6":
            exit()

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
def ShowBooks():
    books = load_books()
    for book in books:
        print(book['Название'])

def arithmetic_mean():
    grades = []
    books = load_books()
    for book in books:
        grades.append(int(book['Оценка']))
    result = sum(grades) / len(grades)
    print(f"Средняя оценка: {result}")

def authors_count():
    books = load_books()
    result = {

    }

    for book in books:
        if book['Автор'] in result.keys():
            result[book['Автор']] += 1
        else:
            result[book['Автор']] = 1
    
    print("Статистика по авторам:")
    for i in result.keys():
        print(f"Автор: {i}, Книги: {result[i]}")
def delete():
    books = load_books()
    index = 0
    print("Выберете книгу для удаления.")
    for book in books:
        print(f"{index}. {book['Название']}.")
        index += 1
    result = int(input(">"))
    books.pop(result)
    save_books(books)

if __name__ == "__main__":
    main()