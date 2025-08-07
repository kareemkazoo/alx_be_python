from book_class import book

def main():
    my_book = book("1984", "George Orwell", 1949)
    
    print(my_book)  
    
    print(repr(my_book))
    
    del my_book

if __name__ == "__main__":
    main()