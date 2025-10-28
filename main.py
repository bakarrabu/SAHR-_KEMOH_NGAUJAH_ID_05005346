from library_functions import *

books = {}
members = []
genres = ("Fiction", "Sci-Fi", "Non-fiction", "Poetry")

# Add some books
add_book(books, "978001", "Matilda", "Roald Dahl", genres[0], 4)
add_book(books, "978002", "The Hobbit", "J.R.R. Tolkien", genres[1], 2)

# Add members
add_member(members, "M001", "Aisha Conteh", "aisha@example.com")

# Borrow and return
borrow_book(books, members, "M001", "978002")
return_book(books, members, "M001", "978002")

# Search
search_book(books, "Hobbit")

# Try deleting
delete_book(books, "978001")

# Print current state
print("\n📚 Current Library Books:")
for k, v in books.items():
    print(k, "=>", v)

print("\n👥 Members List:")
for m in members:
    print(m)