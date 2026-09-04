def issue_book(book):
    if book[3]=="Available":
        book[3]="Issued"
        print("Book issued")
    else:
        print("Book not available")

def return_book(book):
    book[3]="Available"
    print("Book returned")
