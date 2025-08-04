class Book:
    def __init__(self, title, author):
        self.title = title  # خاصية عامة
        self.author = author  # خاصية عامة
        self._is_checked_out = False  # خاصية خاصة (مش بنعرضها مباشرة)

    def check_out(self):
        """يخلي حالة الكتاب 'غير متاح'"""
        self._is_checked_out = True

    def return_book(self):
        """يرجع الكتاب ويخليه متاح"""
        self._is_checked_out = False

    def is_available(self):
        """يرجع True لو الكتاب متاح"""
        return not self._is_checked_out

    def __str__(self):
        """التمثيل النصي للكتاب لما نطبعه"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        self._books = []  # قائمة خاصة لتخزين الكائنات من نوع Book

    def add_book(self, book):
        """يضيف كتاب جديد للمكتبة"""
        self._books.append(book)

    def check_out_book(self, title):
        """يبحث عن الكتاب بالعنوان ويعمله check out"""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out '{title}'.")
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        """يرجع كتاب للرف"""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned '{title}'.")
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """يطبع كل الكتب المتاحة فقط"""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")
