import random
from swarm import Swarm
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

x_max = 4.5
x_min = -4.5

y_max = 4.5
y_min = -4.5

# def f(x:float,y:float)->...:
#     return (1.5 - x -x*y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x*y**3)**2

def f(x:float, y:float)->...:
    return (1-x)**2 + 100*(y-x**2)**2

if __name__ == "__main__":
    s = Swarm(f, 1000, inertia= random.random(),cognitive=1, social=1,  stop=0.01)
    s.initialize()
    # fig = plt.figure()
    # ax = plt.axes(projection='3d')

    # # x = [particle.position.x for particle in s.particles]
    # # y = [particle.position.y for particle in s.particles]
    # # z = [particle.position.z for particle in s.particles]
    # # ax.scatter3D(x, y, z, c=z, cmap='plasma')

    # X, Y = np.meshgrid(np.linspace(-4.5, 4.5, 1000), np.linspace(-4.5, 4.5, 1000))
    # Z = f(X, Y)
    # ax.plot_surface(X, Y, Z, cmap='binary')

    # # ax.set_xlabel('x')
    # # ax.set_ylabel('y')
    # # ax.set_zlabel('z')
    # # plt.show()
    # s.run()
    
    # x = [particle.position.x for particle in s.particles]
    # y = [particle.position.y for particle in s.particles]
    # z = [particle.position.z for particle in s.particles]
    # ax.scatter3D(x, y, z, c=z, cmap='viridis')

    # plt.show()

    # plt.ion()
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    # # for k in range(150):
    s.run()
    # x = [particle.position.x for particle in s.particles]
    # y = [particle.position.y for particle in s.particles]
    # z = [particle.position.z for particle in s.particles]
    # ax.scatter3D(x, y, z, c=z, cmap='viridis')
    # plt.draw()
    # plt.pause(0.5)
    # ax.cla()