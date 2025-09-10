n = int(input("Enter number of Books in the library: "))
books={}
for i in range(n):
    bookId = input(f"Enter book Id {i+1}: ")
    bookTitle = input(f"Enter book name {i+1}: ")
    books[bookId]=bookTitle
choice=int(input("1.Add Book\n2.Remove Book\n3.Search Book\n4.Update\n5.display all books\n6.count of books\n7book exist(reverse lookup)\n8.Exit\nEnter your choice:"))
while choice!=8:
    if choice==1:
        print("enter the book to be added:")
        bookId,bookTitle=input("enter book id and title:").split(" ")
        books[bookId]=bookTitle
    elif choice==2:
        bookId=input("enter the bookid of book to be removed:")
        books.pop(bookId)
    elif choice==3:
        bookId=input("enter the bookid of book to be searched:")
        if bookId in books:
            print(f"Book found: {books[bookId]}")
        else:
            print("Book not found")
    elif choice==4:
        bookId=input("enter the bookid of book to be updated:")
        if bookId in books:
            bookTitle=input("enter the new title of the book:")
            books[bookId]=bookTitle
        else:
            print("Book not found")
    elif choice==5:
        print("Books in the library:")
        for bookId,bookTitle in books.items():
            print(f"Book ID: {bookId}, Book Title: {bookTitle}")
    elif choice==6:
        print("Total number of books in the library:",len(books))
    elif choice==7:
        bookId=input("enter the bookid of book to be searched:")
        if bookId in books:
            print("Book exists in the library")
        else:
            print("Book does not exist in the library")
    elif choice==8:
        break
    else:
        print("Invalid choice")
    choice=int(input("1.Add Book\n2.Remove Book\n3.Search Book\n4.Update\n5.display all books\n6.count of books\n7book exist(reverse lookup)\n8.Exit\nEnter your choice:"))

        

