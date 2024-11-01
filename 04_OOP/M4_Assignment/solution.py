class Book:
    royalty_rate = 10 

    def __init__(self, title, author, publisher, price):
        self._title = title
        self._author = author
        self._publisher = publisher
        self._price = price

    def get_info(self):
        return self._title, self._author

    def set_info(self, title, author):
        self._title = title
        self._author = author

    def calculate_royalty(self, books_sold):
        if books_sold <= 500:
            royalty = 10
        elif books_sold <= 1000:
            royalty = 12.5
        else:
            royalty = 15
        
        royalty_amount = (self._price * royalty / 100) * books_sold
        return royalty_amount

    def __str__(self):
        return f"Book: {self._title}, Author: {self._author}, Publisher: {self._publisher}, Price: {self._price}"

class Ebook(Book):
    def __init__(self, title, author, publisher, price, ebook_format):
        super().__init__(title, author, publisher, price)  
        self.ebook_format = ebook_format  

    def calculate_royalty(self, books_sold):
        # Calculate royalty without GST deduction for ebooks
        if books_sold <= 500:
            royalty = 10
        elif books_sold <= 1000:
            royalty = 12.5
        else:
            royalty = 15
        
        royalty_amount = (self._price * royalty / 100) * books_sold

        # Deduct 12% GST on the royalty amount
        gst_deduction = 0.12 * royalty_amount
        net_royalty_amount = royalty_amount - gst_deduction
        
        return net_royalty_amount

    def __str__(self):
        return f"Ebook: {self._title}, Author: {self._author}, Publisher: {self._publisher}, Price: {self._price}, Format: {self.ebook_format}"

# book

book1 = Book("Python Programming", "John Doe", "Tech Books", 500)
print(book1)
print(f"Royalty for selling 600 copies: Rs.{book1.calculate_royalty(600):.2f}")


# ebook
ebook1 = Ebook("Python Programming", "Jane Doe", "Tech Books", 500, "PDF")

# Print ebook info
print(ebook1)

# Calculate royalty for different numbers of ebooks sold
books_sold = 600
royalty_amount = ebook1.calculate_royalty(books_sold)
print(f"Royalty for selling {books_sold} copies: Rs.{royalty_amount:.2f}")

books_sold = 1200
royalty_amount = ebook1.calculate_royalty(books_sold)
print(f"Royalty for selling {books_sold} copies: Rs.{royalty_amount:.2f}")
