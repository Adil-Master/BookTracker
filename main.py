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