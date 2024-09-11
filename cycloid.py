from math import sin, cos, atan, pi
import FreeCAD as App
import Part
import Sketcher

# Parameters of the cycloidal disk

N = 35 # number of Rollers
R = 68 # [mm] radius of the Rotor
R_r = 3.3 # [mm] radius of the Rollers
E = 1.5 # [mm] excentricity (or offset) from the input shaft to the center of the rotor
steps = 5000 # number of points on the parametrization


debugging = False


def rescale_func(x, factor=0.7):
    # choose factor between 0 and 1
    return x + factor * sin(x * (N - 1) * 2 * pi +  pi) / (2 * (N - 1) *  pi)

class Epitrochoid:
    def __init__(self,R,R_r,E,N):
        self.N = N # number of Rollers
        self.R = R # radius of the Rotor
        self.R_r = R_r # radius of the Rollers
        self.E = E # excentricity (or offset) from the Input Shaft to the center of the Rotor
        
    def psi(self, theta):
        return atan(sin((self.N - 1)*theta) / ((self.R / (self.E * self.N)) - cos((self.N - 1)*theta)))
    
    def x(self,theta):
        Psi = self.psi(theta)
        return self.R * cos(theta) - self.R_r * cos(theta - Psi) - self.E * cos(self.N * theta)
    
    def y(self,theta):
        Psi = self.psi(theta)
        return - self.R * sin(theta) + self.R_r * sin(theta - Psi) + self.E * sin(self.N * theta)

class EpitrochoidSketcher:
    def __init__(self,epitrochoid,steps=1000):
        self.steps = steps
        self.epitrochoid = epitrochoid
        self.doc = App.ActiveDocument
        self.sketch = self.doc.addObject("Sketcher::SketchObject", "Cycloid")
        
    def run(self):
        # generate coordinates
        # thetaList = [j / self.steps * 2 * pi for j in range(self.steps + 1)]
        thetaList = [rescale_func(j / self.steps, 0.8) for j in range(self.steps + 1)]
        # thetaList = [rescale_func(theta, 0.8) for theta in thetaList]
        xList = [epi.x(theta * 2 * pi) for theta in thetaList]
        yList = [epi.y(theta * 2 * pi) for theta in thetaList]
        # add lines to the sketch
        for j in range(self.steps):
            x1, x2 = xList[j:j+2]
            y1, y2 = yList[j:j+2]
            self.sketch.addGeometry(Part.LineSegment(App.Vector(x1, y1, 0),
                                        App.Vector(x2, y2, 0)), False)
        self.sketch.addConstraint(Sketcher.Constraint("Coincident", 0, 1, self.steps - 1, 2))
        self.doc.recompute()
    

epi = Epitrochoid(R,R_r,E,N)
es = EpitrochoidSketcher(epi,steps)
es.run()

if debugging:
    try:
        import matplotlib.pyplot as plt
        thetaList = [j / 1000 * 2 * pi for j in range(1000)]
        xList = [epi.x(theta) for theta in thetaList]
        yList = [epi.y(theta) for theta in thetaList]
        fig, ax = plt.subplots(figsize=(7,7))
        plt.plot(xList,yList)
        plt.show()
    except:
        App.Console.PrintError("Install matplotlib and / or numpy for debugging mode to work.")
