from manim import *


class DotProduct(Scene):
    def construct(self):

        plane = NumberPlane()
        a = np.array([5,1,0])
        b = np.array([2,2,0])
        proj = a * np.dot(a,b)/np.dot(a,a)

        

        aa = Vector(a)
        bb = Vector(b)
        theta = Angle(aa, bb, radius=1)
        projj = Vector(proj)
        dist1 = Line(a,b)
        dist2 = Line(b,proj)
        

        self.add(plane)
        self.play(Write(aa))
        self.play(Write(bb))
        self.play(Write(theta))
        self.play(Write(projj))
        self.play(Write(dist1))
        self.play(Write(dist2))
        


        self.wait()