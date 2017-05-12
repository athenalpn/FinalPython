"""Using OOP principles:
Rectangle class calculates the perimeter and area measurements when length and width are input. 
Input values are automatically turned into a floating point value. 
Accepts the length and width as direct input to calc the area and perimeter of the rectangle.
or accept the coordinates of the top left and bottom right corners
Prints out whether the object is a square.

* User Instructions:
For the main program, Enter a length and a width first to determine if a square by those values
Next you will enter coordinates for top left and bottom right, e.g. 2,2 or 3,5 
be sure to include the comma and no spaces.
It will tell you by either input if a square or not. 

"""
class Rectangle:
    """Accepts either length and width as direct input or 
           accepts only the coordinates of the top left and bottom right corners 
           """
    def __init__(self, top_left=(0, 0), bottom_right=(0, 0), length=0, width=0):


        self.top_left = top_left
        self.bottom_right = bottom_right
        if length == 0:
            self.length = self.get_length()
        else:
            self.length = length
        if width == 0:
            self.width = self.get_width()
        else:
            self.width = width

    def get_length(self):
        """will calculate the length of a rectangle given top left and bottom right coordinate tuples"""
        x1, y1 = self.top_left
        x2, y2 = self.bottom_right
        return abs(x1) + abs(x2)

    def get_width(self):
        """will calculate the width of a rectangle given top left and bottom right coordinate tuples"""
        x1, y1 = self.top_left
        x2, y2 = self.bottom_right
        return abs(y1) + abs(y2)

    def get_perimeter(self):
        """will calculate the perimeter given the length and width of the rectangle"""
        return self.length * 2 + self.width * 2

    def get_area(self):
        """will calculate the area given the length and width of the rectangle"""
        return self.length * self.width

    def is_square(self):
        """will determine whether the rectangle meets the criteria for being a square or not."""
        if self.length == self.width:
            return True
        else:
            return False

if __name__ == '__main__':

    print("Enter length: ")
    l = int(input())
    print("Enter the width: ")
    w = int(input())
    theRectangle = Rectangle(length=l, width=w)
    print(theRectangle.get_area())
    print(theRectangle.get_perimeter())
    print("This is a square: ", theRectangle.is_square())

    print("Enter two numbers for first coordinates: ")
    first = tuple(map(int, input().split(',')))
    print("Enter two numbers for second coordinates: ")
    second = tuple(map(int, input().split(',')))
    theRectangle = Rectangle(first, second)
    print(theRectangle.get_area())
    print(theRectangle.get_perimeter())
    print(theRectangle.is_square())



