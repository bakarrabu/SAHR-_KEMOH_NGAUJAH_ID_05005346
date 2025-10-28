from library_functions import *

# Function to test all features
def test_cases():
    books = {}
    members = []

    add_book(books, "001", "Matilda", "Roald Dahl", "Fiction", 3)
    add_member(members, "M001", "Sahr Kemoh", "sahr@example.com")

    borrow_book(books, members, "M001", "001")
    assert books["001"]["available"] == 2, "Book availability not updated!"

    return_book(books, members, "M001", "001")
    assert books["001"]["available"] == 3, "Book not returned properly!"

    delete_book(books, "001")
    assert "001" not in books, "Book not deleted!"

    print("\n✅ All test cases passed successfully!")

# 👇 This will run automatically when you press Run in PyCharm
test_cases()