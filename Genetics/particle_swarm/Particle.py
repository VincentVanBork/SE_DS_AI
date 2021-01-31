import random

from Matrix import Matrix
class Particle:
    position:Matrix
    velocity:Matrix
    bestPosition:Matrix    # Personal best solution.
    bestEval:Matrix        # Personal best value.
    function = None  # The evaluation function to use.
    def __init__(self, func, beginRange, endRange) -> None:
        super().__init__()
        if (beginRange >= endRange):
            raise ValueError("Begin range must be less than end range.")
        self.function = func
        self.position = Matrix()
        self.velocity = Matrix()
        self.setRandomPosition(beginRange, endRange)
        self.bestPosition = self.velocity.clone()
        self.bestEval = self.evaluate()
    
    def evaluate(self):
        return self.function(self.position.x, self.position.y)

    def setRandomPosition (self, beginRange, endRange):
        x = random.uniform(beginRange, endRange)
        y = random.uniform(beginRange, endRange)
        z = random.uniform(beginRange, endRange)
        self.position.x = x
        self.position.y = y
        self.position.z = z
    
    def updatePersonalBest(self):
        evaluation = self.evaluate()
        if (evaluation < self.bestEval):
            self.bestPosition = self.position.clone()
            self.bestEval = evaluation

    def updatePosition(self):
        self.position.add(self.velocity)
    