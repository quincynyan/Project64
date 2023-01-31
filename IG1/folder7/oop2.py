from typing import Optional

class Shape:
    def __init__(self, color: str):
        self.color = "black"

    def display_color(self):
        print(f"Color is {self.color}")


class Rectangle(Shape):
    def __init__(self, length: float, width: Optional[float] = None, color: str = "green"):
        self.length = length
        self.width = width or self.length
        self.color = color

    def display_area(self):
        print(f"Area is {self.length * self.width}")


def main():
    print("Hello world!")

    rect = Rectangle(10, 4, "cyan")
    rect.display_color()
    rect.display_area()

    square = Rectangle(10)
    square.display_color()
    square.display_area()


if __name__ == "__main__":
    main()