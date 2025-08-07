from library_system import Book, EBook, PrintBook, Library

def main():
    # إنشاء مكتبة
    my_library = Library()

    # إنشاء كتب بأنواع مختلفة
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # إضافة الكتب للمكتبة
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # عرض كل الكتب
    my_library.list_books()

if __name__ == "__main__":
    main()
