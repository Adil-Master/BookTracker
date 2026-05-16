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