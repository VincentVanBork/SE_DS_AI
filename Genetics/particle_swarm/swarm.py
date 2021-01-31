from Particle import Particle
from Matrix import Matrix
import numpy as np
import random
import matplotlib.pyplot as plt


class Swarm:

    DEFAULT_STOP_CONDITION = 0.000001 
    numOfParticles:int
    inertia:float
    cognitiveComponent:float 
    socialComponent:float
    bestPosition:Matrix
    bestEval:float
    function = None
     # The function to search.
    DEFAULT_INERTIA = 0.729844
    DEFAULT_COGNITIVE = 1.496180 # Cognitive component.
    DEFAULT_SOCIAL = 1.496180 # Social component.

    beginRange:float 
    endRange:float
    DEFAULT_BEGIN_RANGE = -1.5
    DEFAULT_END_RANGE = 1.5


    """*
     * Construct the Swarm with custom values.
     * @param particles     the number of particles to create
     * @param inertia       the particles resistance to change
     * @param cognitive     the cognitive component or introversion of the particle
     * @param social        the social component or extroversion of the particle
     * @param STOP_CONDITION as name suggests
     * @param out type of outing irrelevant for algorithm necceasry for server
     """
    def __init__(self, func, particles=None, inertia=None, cognitive=None, social=None, stop=None, begin=None, end=None) -> None:
        super().__init__()
        if particles:
            self.numOfParticles = particles
        else:
            self.numOfParticles = 100

        if inertia:
            self.inertia = inertia
        else:
            self.inertia = self.DEFAULT_INERTIA
        if cognitive:
            self.cognitiveComponent = cognitive
        else:
            self.cognitiveComponent = self.DEFAULT_COGNITIVE
        if social:
            self.socialComponent = social  
        else:
            self.socialComponent = self.DEFAULT_SOCIAL
        
        self.function = func
        if stop:
            self.STOP_CONDITION = stop
        else:
            self.STOP_CONDITION = self.DEFAULT_STOP_CONDITION

        self.bestPosition =  Matrix(np.inf, np.inf, np.inf)
        self.bestEval = np.inf
        if begin:
            self.beginRange = begin
        else:
            self.beginRange = self.DEFAULT_BEGIN_RANGE
        if end: 
            self.endRange = end
        else:
            self.endRange = self.DEFAULT_END_RANGE
        self.particles = []
        self.generation = 0

        self.holdup = 0
        self.Rad = []


    """*
     * algorithm.
     * stop condition is chosen so that average swarm radius is smaller than some given value
     """
    def run(self):

        self.oldEval = self.bestEval

        Rad = self.Rad
        generation = self.generation
        holdup = self.holdup
        
        self.updateRadius(Rad)
        R0 = max(Rad)
        print("MAX radius",R0)
        R = max(Rad)
        print("alone R", R)
        print("R to R0", R/R0)
        plt.ion()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        while(R/R0 > self.STOP_CONDITION):
            if (R/R0 > 10000):
                break
            print("R to R0", R/R0)
            generation += 1
            if self.bestEval == self.oldEval:
                holdup += 1
                print(holdup)
                print(self.bestEval)
                print(f"Hold up number :  {holdup} at  {self.bestEval} with x,y {self.bestPosition.x},{self.bestPosition.y}")

            if self.bestEval < self.oldEval:
                holdup = 0

                print(f"Global Best Evaluation (Epoch {generation + 1} :\t + {self.bestEval}")
                self.oldEval = self.bestEval
            

            for p in self.particles:
                p.updatePersonalBest()
                self.updateGlobalBest(p)
            

            for p in self.particles:
                self.updateVelocity(p)
                p.updatePosition()
            

            self.updateRadius(Rad)
            R = max(Rad)
            
            # for k in range(150):

            x = [particle.position.x for particle in self.particles]
            y = [particle.position.y for particle in self.particles]
            z = [particle.position.z for particle in self.particles]
            ax.scatter3D(x, y, z, c=z, cmap='viridis')
            plt.draw()
            plt.pause(0.5)
            ax.cla()

        print("RESULT")
        print(f"x =  {self.bestPosition.x}")
        print(f"y =  {self.bestPosition.y}")

        print(f"Final Best Evaluation:  {self.bestEval}")


    """*
     * Create a set of particles, each with random starting positions.
     * @return  an array of particles
     """
    def initialize(self):
        for i in range(self.numOfParticles):
            particle = Particle(self.function, self.beginRange, self.endRange)
            self.particles.append(particle)
            self.updateGlobalBest(particle)

    

    """*
     * Update the global best solution if the specified particle has
     * a better solution
     * @param particle  the particle to analyze
     """
    def updateGlobalBest(self, particle:Particle):
        if particle.bestEval < self.bestEval:
            self.bestPosition = particle.bestPosition
            self.bestEval = particle.bestEval
        

    def updateRadius(self, setR:list):
        setR.clear()
        for p in self.particles:
            x = (p.position.x - self.bestPosition.x )* (p.position.x - self.bestPosition.x)
            y = (p.position.y - self.bestPosition.y )* (p.position.y - self.bestPosition.y)
            R = np.sqrt(x+y)
            setR.append(R)
        

    """*
     * Update the velocity of a particle using the velocity update formula
     * @param particle  the particle to update
     """
    def updateVelocity (self, particle:Particle):
        oldVelocity = particle.velocity
        pBest = particle.bestPosition
        gBest = self.bestPosition.clone()
        pos = particle.position

 
        r1 = random.random()
        r2 = random.random()
        while r2 == r1:
            r2 = random.random()
        

        # The first product of the formula.
        newVelocity = oldVelocity.clone()
        newVelocity.mul(self.inertia)

        # The second product of the formula.
        pBest.sub(pos)
        pBest.mul(self.cognitiveComponent)
        pBest.mul(r1)
        newVelocity.add(pBest)

        # The third product of the formula.
        gBest.sub(pos)
        gBest.mul(self.socialComponent)
        gBest.mul(r2)
        newVelocity.add(gBest)

        particle.velocity = newVelocity