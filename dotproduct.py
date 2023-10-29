from manim import *

class Start(Scene):
    def construct(self):
        
        ax = Axes(axis_config={"include_ticks":False})

        a = np.array([2,2,0])
        b = np.array([4,-1,0])
        t_a = MathTex(r"a")
        t_b = MathTex(r"b")

        f_1 = MathTex(r"\| a \| = \sqrt{x_a^2 + y_a^2}")
        f_2 = MathTex(r"\| b \| = \sqrt{x_b^2 + y_b^2}")
        f_3 = MathTex(r"a \cdot b = x_a x_b + y_a y_b")
        f_4 = MathTex(r"a \cdot b = \|a\|\|b\| \cos \theta")

        x_a = np.array([2,0,0])
        y_a = np.array([0,2,0])
        x_b = np.array([4,0,0])
        y_b = np.array([0,-1,0])

        aa = Vector(a)
        bb = Vector(b)

        line_1 = DashedLine(aa.get_end(), x_a )
        line_2 = DashedLine(aa.get_end(), y_a )
        line_3 = DashedLine(bb.get_end(), x_b )
        line_4 = DashedLine(bb.get_end(), y_b )

        label_a = aa.coordinate_label()
        label_b = bb.coordinate_label()

        angle = Angle(aa, bb, other_angle=True, radius=1)
        # angle.add_updater(lambda m, dt: m.become(Angle(ax.x_axis, aa)))
        # angle.update()

        self.add(ax, aa, bb)

        self.add(t_a.next_to(aa.get_center(), UL, buff=SMALL_BUFF))
        self.add(t_b.next_to(bb.get_center(), DL, buff=SMALL_BUFF))

        self.play(Write(label_a), Write(label_b))
        self.add(line_1, line_2, line_3, line_4)

        self.play(Write(f_1.to_edge(UL, buff=LARGE_BUFF)))
        self.play(Write(f_2.next_to(f_1, DOWN)))
        self.play(Write(f_3.next_to(f_2, DOWN)))

        self.play(Write(f_4.to_edge(DL, buff=LARGE_BUFF)))

        self.play(Write(angle))

        self.wait(10)

class Cosine(Scene):
    def construct(self):

        ax = Axes()
        
        a = np.array([2,3,0])
        b = np.array([3,1,0])

        aa = Vector(a)
        bb = Vector(b)

        angle_a = Angle(aa, ax.x_axis, other_angle=True, radius=0.5)
        angle_a.add_updater(lambda m: m.become(Angle(aa, ax.x_axis, other_angle=True, radius=0.5)))

        angle_b = Angle(bb, ax.x_axis, other_angle=True, radius=0.7)
        angle_b.add_updater(lambda m: m.become(Angle(bb, ax.x_axis, other_angle=True, radius=0.7)))

        r_a = np.linalg.norm(a)
        r_b = np.linalg.norm(b)

        theta_a = np.arccos(a[0]/r_a)
        theta_b = np.arccos(b[0]/r_b)



        self.add(ax)       

        self.play(Write(aa))
        self.play(Write(angle_a))
        
        self.play(Write(bb))
        self.play(Write(angle_b))

        self.play(bb.animate.rotate(-theta_b, about_point=bb.get_start()))
        self.play(aa.animate.rotate(-theta_a, about_point=aa.get_start()))

        
        
        self.wait()


class DotProduct(Scene):
    def construct(self):

        plane = NumberPlane()
        # self.add(plane)
        
        vt = ValueTracker(-1)
        line_0 = Line(ORIGIN, [3, 0, 0]).set_color(YELLOW)
        # line_1 = Line(ORIGIN, [0, 1, 0]).add_updater(lambda m: m.become(Line(ORIGIN, [-2*np.sin(vt.get_value()), 2*np.cos(vt.get_value()), 0]).set_color(BLUE)))
        line_1 = Line(ORIGIN, [0, 1, 0]).add_updater(lambda m: self.my_fun(m, vt))
        proj = Line(ORIGIN, line_1.get_end()).add_updater(lambda m: self.my_proj(m, line_1, vt))
        angle = Angle(line_0, line_1).add_updater(lambda m: m.become(Angle(line_0, line_1)))

        number = DecimalNumber(0, color=RED).to_corner().add_updater(lambda m: self.my_num(m, line_1))

        self.add(line_0, line_1, angle, proj, number)
        self.play(vt.animate.set_value(10), run_time=20, rate_func=linear)

    def my_fun(self, mob, vt):

        return mob.become(Line(ORIGIN, [-2*np.sin(vt.get_value()), 2*np.cos(vt.get_value()), 0]).set_color(BLUE))
    
    def my_num(self, m, line_1):
        a = line_1.get_end()
        b = np.array([3,0,0])
        tmp = a * np.dot(a,b)/np.dot(a,a)
        tmp = b * np.dot(a,b)/np.dot(b,b)

        return m.set_value(np.dot(a,b))
    
    def my_proj(self, mob, line_1, vt):
        a = line_1.get_end()
        b = np.array([3,0,0])
        tmp = a * np.dot(a,b)/np.dot(a,a)
        tmp = b * np.dot(a,b)/np.dot(b,b)
        return mob.become(Line(line_1.get_end(), tmp))