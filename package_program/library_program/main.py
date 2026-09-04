from books.book import add_book,display_books
from members.member import add_member,display_members
from transactions.transaction import issue_book,return_book

books=[]
members=[]

books.append(add_book(101,"Python","John"))
books.append(add_book(102,"Java","James"))

members.append(add_member(1,"Amit"))
members.append(add_member(2,"Priya"))

print("Books:")
display_books(books)

print("\nMembers:")
display_members(members)

print("\nTransactions:")
issue_book(books[0])
print(books[0])
return_book(books[0])
print(books[0])
