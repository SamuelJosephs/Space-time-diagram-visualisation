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
        s_prime.target.apply_matrix([[math.cos(math.atan(0.5)),math.sin(math.atan(0.5))],[math.sin(math.atan(0.5)),math.cos(math.atan(0.5))]])
        
        self.play(Create(s))
        self.add(s_prime)

        #Updaters

        beta = DecimalNumber(0).to_corner(UR)
        text = MathTex("\\beta = ").to_corner(UR).shift([-1,0,0])
        tracker = ValueTracker(0)

        beta.add_updater(lambda x: x.set_value(tracker.get_value()))




        def s_prime_updater(obj):

            s_prime_2 = NumberPlane(x_range = [-100,100],y_range = [-100,100])
            s_prime_2.set_color(GREEN)
            s_prime_2.axes[0:2].set_color(WHITE)
            obj.become(s_prime_2.apply_matrix([[math.cos(math.atan(tracker.get_value())),math.sin(math.atan(tracker.get_value()))],[math.sin(math.atan(tracker.get_value())),math.cos(math.atan(tracker.get_value()))]]))
             
        s_prime.add_updater(s_prime_updater)

        self.add(s_prime,beta,text)

        self.play(tracker.animate.set_value(0.9),rate_func = linear,run_time = 6)
        
        self.wait(1)

        
        
        self.play(tracker.animate.set_value(0.5),rate_func = linear, run_time = 4)
        self.wait(2)

        