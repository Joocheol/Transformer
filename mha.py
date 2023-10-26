from manim import *

class Start(Scene):
    def construct(self):

        sq = Square().set_fill(YELLOW, opacity=0.8).scale(0.1)
        rect_1 = Rectangle(width=10).set_fill(BLUE, opacity=0.8).scale(0.1)
        rect_2 = Rectangle(width=2, height=10).set_fill(RED, opacity=0.8).scale(0.1)
        mat = VGroup(*[VGroup(*[sq.copy() for _ in range(5)]).arrange(DOWN) for _ in range(5)]).arrange(RIGHT)
        
        left = VGroup(*[rect_1.copy() for _ in range(5)]).arrange(DOWN).next_to(mat, LEFT)
        right = VGroup(*[rect_2.copy() for _ in range(5)]).arrange(RIGHT).next_to(mat, DOWN)
        
        self.play(Write(mat))
        self.wait()
        self.play(Write(left))
        self.play(Write(right))


        self.wait()