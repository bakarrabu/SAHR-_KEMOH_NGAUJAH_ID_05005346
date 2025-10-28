def add_book(books, isbn, title, author, genre, total):
    if isbn in books:
        print("Book already exists!")
    else:
        books[isbn] = {"title": title, "author": author, "genre": genre, "total": total, "available": total}
        print(f"Book '{title}' added successfully.")

def add_member(members, member_id, name, email):
    for m in members:
        if m['id'] == member_id:
            print("Member already exists!")
            return
    members.append({"id": member_id, "name": name, "email": email, "borrowed": []})
    print(f"Member '{name}' added successfully.")

def search_book(books, query):
    found = [info for info in books.values() if query.lower() in info['title'].lower() or query.lower() in info['author'].lower()]
    if found:
        for f in found:
            print(f"Found: {f['title']} by {f['author']} ({f['genre']})")
    else:
        print("No book found.")

def borrow_book(books, members, member_id, isbn):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member:
        print("Member not found!")
        return
    if isbn not in books:
        print("Book not found!")
        return
    if books[isbn]["available"] == 0:
        print("Book not available!")
        return
    if len(member["borrowed"]) >= 3:
        print("Borrow limit reached (3 books)!")
        return
    books[isbn]["available"] -= 1
    member["borrowed"].append(isbn)
    print(f"{member['name']} borrowed '{books[isbn]['title']}'.")

def return_book(books, members, member_id, isbn):
    member = next((m for m in members if m["id"] == member_id), None)
    if not member or isbn not in member["borrowed"]:
        print("No record of this book being borrowed.")
        return
    books[isbn]["available"] += 1
    member["borrowed"].remove(isbn)
    print(f"{member['name']} returned '{books[isbn]['title']}'.")

def delete_book(books, isbn):
    if isbn in books and books[isbn]["available"] == books[isbn]["total"]:
        del books[isbn]
        print("Book deleted successfully.")
    else:
        print("Cannot delete. Some copies are still borrowed.")
