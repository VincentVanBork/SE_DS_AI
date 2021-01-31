
import random
from math import sqrt

def get_next_letter(maxLetter):
    current = 0
    while current < maxLetter:
        yield chr(ord('a') + current)
        current += 1


class point:
    def __init__(self, letter) -> None:
        self.letter = letter
        self.create_random()
        
    def create_random(self, Xran=(-100,100), Yran=(-100,100), Zran=(-50,50)):
        self.x = random.uniform(Xran[0], Xran[1])
        self.y = random.uniform(Yran[0], Yran[1])
        self.z = random.uniform(Zran[0], Zran[1])

    def calculate_distance_to(self, other_point):
        return sqrt((self.x - other_point.x )**2 +(self.y - other_point.y)**2 +(self.z - other_point.z )**2 )


class graph:
    def __init__(self, numNodes) -> None:
        self.num = numNodes
        self.points = [point(letter) for letter in get_next_letter(self.num)]
        self.all = {point.letter: [other_node.letter for other_node in self.points if other_node.letter != point.letter] for point in self.points}
        self.current = self.all

    def get_node(self, letter):
        for point in self.points:
           if point.letter == letter:
               return point

    def remove_node(self, letter):
        for key, value in self.current.items():
            for some_node in value:
                if some_node == letter:
                    value.remove(some_node)
                    
    def reset_graph(self):
        print(self.current)
        print(self.all)
        original = self.all.copy()
        self.current = original
        
        print(self.current)
        print(self.all)


class graph_path:
    def __init__(self, start) -> None:
        super().__init__()
        self.value = None
        self.order = start

# g = graph(5)
# for point in g.points:
#     print(point.letter) 
# print(g.all)
# letter = get_next_letter()
# print(next(letter))
# print(next(letter))
# print(next(letter))
# for let in get_next_letter():
#     print(let)


