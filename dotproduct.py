from manim import *

class DotProduct(VectorScene):
    def construct(self):

        plane = self.add_plane(animate=True)
        a = self.add_vector([2,1])

        self.wait()