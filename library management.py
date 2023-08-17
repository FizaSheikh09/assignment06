#using single-inheritance concept in this library management example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.books_borrowed = []

    def borrow_book(self, book_title):
        self.books_borrowed.append(book_title)
        print(f"{self.name} has borrowed '{book_title}'.")

    def return_book(self, book_title):
        if book_title in self.books_borrowed:
            self.books_borrowed.remove(book_title)
            print(f"{self.name} has returned '{book_title}'.")
        else:
            print(f"{self.name} did not borrow '{book_title}'.")

    def display_books_borrowed(self):
        print(f"{self.name}'s borrowed books:")
        for book in self.books_borrowed:
            print(f"  - {book}")


# Main program
if __name__ == "__main__":
    person1 = Person("Ali", 15)
    person1.display_info()

    print("=" * 20)

    student1 = Student("Fiza Sheikh", 20, "ST123")
    student1.display_info()
    student1.borrow_book("Introduction to Python")
    student1.borrow_book("Object Oriented Programming")
    student1.display_books_borrowed()
    student1.return_book("Introduction to Python")
    student1.display_books_borrowed()

