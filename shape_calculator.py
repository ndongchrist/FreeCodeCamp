class Rectangle:
      #created the rectangle class
    def __init__(self, width, height):
        self.width = width
        self.height = height
    #Displaying the rectangle
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
      
    #declaring the widht
    def set_width(self, width):
        self.width = width
      
    #declaring the height
    def set_height(self, height):
        self.height = height
      
    #Computing the Area of the rectangle l*w
    def get_area(self):
        return self.width * self.height
      
    #computing the perimeter of the rectangle
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)
      
    #Returns the diagonal
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5
      
    #To have an image of the figure
    def get_picture(self):

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height
          
    #Returns the number of times shape can fit in a figure
    def get_amount_inside(self, shape):
        EnterHorizontal = self.width // shape.width
        EnterVertical = self.height // shape.height
        return EnterHorizontal * EnterVertical


class Square(Rectangle):#inherits the rectangle class
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)
        pass

    def __repr__(self):
        return f"Square(side={self.side})"

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)




r1 = Rectangle(20, 6)
r1.get_picture()
s1 = Square(5)
s1.set_width = 20
s1.set_height = 5
s1.get_picture()
