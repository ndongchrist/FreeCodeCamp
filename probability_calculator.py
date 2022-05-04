import random


class Hat:
    def __init__(self, red =0,green=0,yellow=0,orange=0,black=0,blue=0,pink=0):
        self.red = red
        self.green = green
        self.yellow = yellow
        self.orange = orange
        self.black = black
        self.blue = blue
        self.pink = pink
        dict = {
            'red':self.red,
            'green': self.green,
            'yellow':self.yellow,
            'orange':self.orange,
            'black':self.black,
            'blue':self.blue,
            'pink':self.pink
        }
        self.content = []

        for key in dict.keys():
            if key == 'red':
                for i in range(dict[key]):
                    self.content.append('red')
            if key == 'green':
                for i in range(dict[key]):
                    self.content.append('green')
            if key == 'yellow':
                for i in range(dict[key]):
                    self.content.append('yellow')
            if key == 'black':
                for i in range(dict[key]):
                    self.content.append('black')
            if key == 'orange':
                for i in range(dict[key]):
                    self.content.append('orange')
            if key == 'blue':
                for i in range(dict[key]):
                    self.content.append('blue')
            if key == 'pink':
                for i in range(dict[key]):
                    self.content.append('pink')
                     

h1 = Hat(yellow=3, blue=2, green=6)        
print(h1.content)