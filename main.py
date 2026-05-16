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

if __name__ == "__main__":
    main()