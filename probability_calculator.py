import random
from select import select


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
    def draw(self, numofBalls):
        removed = []
        if numofBalls < len(self.content):
            for i in range(numofBalls):
                item = self.content[random.randint(0, len(self.content)-1)]
                self.content.remove(item)
                removed.append(item)
        elif numofBalls >= len(self.content):
            removed = removed + self.content 
            self.content.clear()
        return removed

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = Hat()
    sum = 0
    expected_counts = 0
    removedball = hat.draw(num_balls_drawn)
    
    for  i in range(num_experiments):
        for ballcolor,ballnum in expected_balls.items():
            for elmt in range(ballnum):
                if ballcolor in removedball:
                    removedball.remove(ballcolor)
                    expected_balls[ballcolor] -= 1
        
        for value in expected_balls.values():
            sum += value
            if sum == 0:
                expected_counts += 1

    probability = expected_counts / num_experiments
    return probability
    


