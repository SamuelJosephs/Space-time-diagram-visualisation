from PIL.Image import LINEAR
from manim import *
import math

class space_time(Scene):
    def construct(self):

        s = NumberPlane(x_range=[-100,100],y_range = [-100,100])

        s_prime = NumberPlane(x_range =[-100,100],y_range=[-100,100])
        s_prime.set_color(GREEN)
        s_prime.axes[0:2].set_color(WHITE)
        s_prime.generate_target()
        s_prime.target.apply_matrix([[math.cos(math.atan(0.6)),math.sin(math.atan(0.6))],[math.sin(math.atan(0.6)),math.cos(math.atan(0.6))]])
        
        self.play(Create(s))
        self.add(s_prime)

        #Updaters

        beta = DecimalNumber(0).to_corner(UR)
        text = MathTex("\\beta = ").to_corner(UR).shift([-1,0,0])
        tracker = ValueTracker(0)

        beta.add_updater(lambda x: x.set_value(tracker.get_value()))

        
 
        s_prime.add_updater(lambda x: x.become(s_prime.apply_matrix([[math.cos(math.atan(tracker.get_value()) * DEGREES),math.sin(math.atan(tracker.get_value()) * DEGREES)],[math.sin(math.atan(tracker.get_value()) * DEGREES),math.cos(math.atan(tracker.get_value()) * DEGREES)]])))

        self.add(s_prime,beta,text)

        self.play(tracker.animate.set_value(0.95),rate_func = linear,run_time = 6)
        print(tracker.get_value())
        self.wait(1)

        
        s_prime.clear_updaters()
        self.play(Transform(s_prime,s_prime.target),tracker.animate.set_value(0.6),rate_func = linear, run_time = 4)
        self.wait(2)

        