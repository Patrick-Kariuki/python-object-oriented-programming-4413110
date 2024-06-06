# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ('HARDCOVER', 'PAPERBACK', 'EBOOK')

    # TODO: double-underscore properties are hidden from other classes
    # singleton design pattern, global variable for classes to use
    __booktypes = None

    # TODO: create a class method
    # receives the class itself as the first argument
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    # do not the class or instance objects
    def getbooklist():
        if not Book.__booktypes:
            Book.__booktypes = []
        return Book.__booktypes

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype not in Book.BOOK_TYPES:
            raise ValueError(f"{booktype} not a valid book type")
        else:
            self.booktype = booktype


# TODO: access the class attribute
print('Book types:', Book.BOOK_TYPES)

# TODO: Create some book instances
b1 = Book('Title1', 'HARDCOVER')
b2 = Book('Title1', 'PAPERBACK')

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)