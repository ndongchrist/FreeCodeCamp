from xml.etree.ElementPath import get_parent_map


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

        if dict.keys == 'red':
            for i in dict.values():
                self.content.append('red')

h1 = Hat(red=5)        
print(h1.content)