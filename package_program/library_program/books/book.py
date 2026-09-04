def add_book(book_id,title,author):
    return [book_id,title,author,"Available"]

def display_books(books):
    for book in books:
        print(book)
