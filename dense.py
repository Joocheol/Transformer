from manim import *

class S010(Scene):
    def construct(self):

        f_1 = MathTex(r"y = \beta_0 + \beta_1 x")
        f_2 = MathTex(r"y = \beta_0 + \beta_1 x_1 + \beta_2 x_2")
        f_n = MathTex(r"y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n")

        VGroup(f_1, f_2, f_n).arrange(DOWN, buff=1)
        
        self.wait()
        self.play(Write(f_1))
        self.wait()
        self.play(Write(f_2))
        self.wait()
        self.play(Write(f_n))
        self.wait()

class S020(Scene):
    def construct(self):

        f_3 = MathTex(r"y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \beta_3 x_3")

        eq_3 = MathTex(r"\begin{bmatrix} w_1 & w_2 & w_3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3\end{bmatrix} + b")

        VGroup(f_3, eq_3).arrange(DOWN, buff=1)
        
        self.wait()
        self.play(Write(f_3))
        self.wait()
        self.play(Write(eq_3))
        self.wait()

class S030(Scene):
    def construct(self):

        eq_3 = MathTex(r"\begin{bmatrix} w_1 & w_2 & w_3 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3\end{bmatrix} + b")
        eq_n = MathTex(r"""\begin{bmatrix} w_{11} & w_{12} & w_{13} \\
                       w_{21} & w_{22} & w_{23} & \\ & \vdots  & \\
                       w_{\text{units}, 1} & w_{\text{units}, 2} & w_{\text{units}, 3}  
                       \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3  \end{bmatrix} + b""")


        VGroup(eq_3, eq_n).arrange(DOWN, buff=1)
        
        self.wait()
        self.play(Write(eq_3))
        self.wait()
        self.play(Write(eq_n))
        self.wait()

class S090(Scene):
    def construct(self):
        
        cir = Circle(radius=0.2)
        dot = Dot()

        dots = VGroup(*[dot.copy() for _ in range(5)]).arrange(DOWN)
        cirs = VGroup(*[cir.copy() for _ in range(10)]).arrange(DOWN)

        net = VGroup(dots, cirs).arrange(RIGHT, buff=5)

        lines =VGroup()

        for i in cirs:
            for j in dots:
                lines.add(Line(j.get_right(), i.get_left()))

        self.play(Write(net))
        self.wait()
        self.play(Write(lines), run_time=5)
        self.wait()