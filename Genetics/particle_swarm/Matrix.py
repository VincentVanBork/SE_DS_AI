import numpy as np
class Matrix:
    x:float
    y:float
    z:float
    lim = np.inf

    def __init__(self,x=0,y=0,z=0) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.z = z

    def mag(self):
        return np.sqrt(self.x*self.x + self.y*self.y)

    def limit(self):
        m = self.mag()
        if m > self.lim:
            ratio = m / self.limit
            self.x /= ratio
            self.y /= ratio
        
    def add(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
        self.limit()
    

    def sub (self, v):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z
        self.limit()
    

    def mul (self, s):
        self.x *= s
        self.y *= s
        self.z *= s
        self.limit()
    
    def clone (self):
        return Matrix(self.x, self.y, self.z)
    
    def __str__(self):
        return f"x: {self.x}, y: {self.y}, z: {self.z}"
