# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        # double underscores create hidden attributes
        # cannot be seen outside the class
        self.__secret = "This is a secter attribute"

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, '_discount'): # test if class has specified attribute
            return self.price - (self.price * self._discount)
        return self.price
    
    def set_discount(self, amount):
        # underscore signals that attribute is for internal use only
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())


# TODO: try setting the discount
print(b2.getprice())
b2.set_discount(0.1)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter
