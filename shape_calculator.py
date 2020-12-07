class Rectangle:

  def __init__(self,width,height):
    self.width=width
    self.height=height
  def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

  def set_width(self,width):
    self.width=width
  def set_height(self, height):
    self.height=height
  def get_area(self):
    area=self.width*self.height
    return area
  def get_perimeter(self):
    perimeter=2*self.width+2*self.height
    return perimeter
  def get_diagonal(self):
    diagonal=(self.width ** 2 + self.height ** 2) ** .5
    return diagonal
  def get_picture(self):
    h=0
    coph=self.height
    if (self.width or self.height) > 50:
      return "Too big for picture."
    else:
      string=''
      while h<coph:
        coph-=1
        star="*"*self.width+"\n"
        string+=star
      print (string)
  
  def get_amount_inside(self, shape):
        self.shape = shape
        if type(self.shape) == Square:
          num_times = self.get_area()/(self.shape.get_area())
          return int(num_times)
        else:
          num_times = self.get_area()/(self.shape.get_area())
          return int(num_times)

 
class Square(Rectangle):
  def __init__(self, side):
    self.width=side
    self.height=side
    
  def __str__(self):
        return "Square(side={})".format(self.width)
  def set_side(self, side):
    self.width=side
    self.height=side
    return self.width, self.height
  def set_width(self,width):
     self.width=width
     self.height=width
  def set_height(self, height):
    self.height=height
    self.width=height
  
