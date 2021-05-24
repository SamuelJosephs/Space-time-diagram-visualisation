from manim import *
import math


class space_time(Scene):
    def construct(self):
        x_prime_initial = MathTex(
                          "x' = " #0
                          "\\gamma", #1
                          "(", #2
                          "x", #3
                          "-", #4
                          "u", #5
                          "t", #6
                          ")" #7
                    
        
        ).to_edge(UP).shift([-4,0,0])

        x_prime_2 = MathTex(
            "x' = ", #0
            "\\gamma", #1
            "\\left(", #2
            "x", #3
            "-", #4
            
            "{u \\over c}", #5    ############################################################################################################################
             
            "c", #6
            "t", #7
            "\\right)"

        ).to_edge(UP,buff = 2.2).shift([-4,0,0])

        x_prime_3 = MathTex(
            "x' = ", #0
            "\\gamma", #1
            "\\left(", #2
            "x", #3
            "-", #4
            
            "\\beta", #5    
             
            "c", #6
            "t", #7
            "\\right)"

        ).to_edge(UP,buff = 2.2).shift([-4,0,0])




        x_prime_rearrange = MathTex(
            "0 =" #0
            "\\gamma", #1
            "(", #2
            "x", #3
            "-", #4
            "\\beta", #5
            "c", #6
            "t", #7
            ")"

        ).to_edge(UP,buff = 2.2).shift([-4,0,0])

        x_prime_rearrange_2 = MathTex(
            "0 =" #0
            "x", #1
            "-", #2
            "\\beta", #3
            "c", #4
            "t", #5
            

        ).to_edge(UP,buff = 3.2).shift([-4.2,0,0])

        x_prime_rearrange_3 = MathTex(
            "ct =" #0
            "{\\beta \\over x}", #3
        
            
            

        ).to_edge(UP,buff = 3.2).shift([-4.2,0,0])

       
        
        t_prime = MathTex(
            "t' = " #0
            "\\gamma", #1
            "\\left(", #2
            "t", #3
            "-", #4
            "{ ux", #5
            "\\over c^2 } ", #6 
            "\\right)" #7
        ).to_edge(UP).shift([4,0,0])

        t_prime_2 = MathTex(
            "ct' = ", #0
            "\\gamma", #1
            "\\left(", #2
            "ct", #3 
            "-", #4
            "{u \\over", #5
            "c}", #6
            "x", #7
            "\\right)" #8
        ).to_edge(UP,buff = 2.2).shift([4,0,0])

        t_prime_3 = MathTex(
            "ct' = ", #0
            "\\gamma", #1
            "(", #2
            "ct", #3 
            "-", #4
            "\\beta", #5
            "x", #6
            ")" #7
        ).to_edge(UP,buff = 2.2).shift([4,0,0])

        t_prime_4 = MathTex(
            "0 = ", #0
            "\\gamma", #1
            "(", #2
            "ct", #3 
            "-", #4
            "\\beta", #5
            "x", #6
            ")" #7
        ).to_edge(UP,buff = 2.2).shift([4,0,0])

        t_prime_5 = MathTex(
            "0 = ", #0
            "ct", #1
            "-",  #2
            "\\beta", #3 
            "x" #4
            
        ).to_edge(UP,buff = 3.2).shift([4,0,0])

        t_prime_6 = MathTex(
            "ct", #0
            "=",  #1
            "\\beta", #2  
            "x"  #3
            
        ).to_edge(UP,buff = 3.2).shift([4,0,0])

        s = NumberPlane(x_range = [-5,5],y_range = [-5,5]).shift([-2,0,0])
        background_coords = NumberPlane(x_range = [-20,20],y_range = [-20,20]).center()
        s_prime = NumberPlane(x_range = [-4,4],y_range = [-4,4]).shift([-2,0,0])
        self.play(Create(s),run_time = 4)
        tracker = ValueTracker(0)
        
        beta = DecimalNumber(0,num_decimal_places= 3).to_corner(UR)
        text = MathTex("{v \\over c} =").to_corner(UR).next_to(beta,LEFT).set_color(GREEN)
        text_2 = MathTex("\\beta = ").to_corner(UR).next_to(beta,LEFT).set_color(GREEN)

        y = MathTex("ct").move_to(s.coords_to_point(-0.5,3.85))
        x = MathTex("x").move_to(s.coords_to_point(5.1,0))

        y_prime = MathTex("ct'").set_color(GREEN)
        x_prime = MathTex("x'").set_color(GREEN)

        self.play(Create(beta),Create(text))

        def s_prime_updater(obj):
            s_prime_2 = NumberPlane(x_range=[-4,4],y_range=[-4,4])
            s_prime_2.set_color(GREEN)
            s_prime_2.axes[0:2].set_color(WHITE)
            obj.become(s_prime_2.apply_matrix([[math.cos(math.atan(tracker.get_value())),math.sin(math.atan(tracker.get_value()))],[math.sin(math.atan(tracker.get_value())),math.cos(math.atan(tracker.get_value()))]]).shift([-2,0,0]))
            #obj.move_to(background_coords.get_center())

        beta.add_updater(lambda x: x.set_value(tracker.get_value()))


            


        s_prime.add_updater(s_prime_updater)
        y_prime.add_updater(lambda x: x.move_to(s_prime.coords_to_point(0,4.3)))
        x_prime.add_updater(lambda x: x.move_to(s_prime.coords_to_point(4.3,0)))
        
        self.add(beta,x_prime,y_prime,y,x)

        self.add(s_prime)
        self.wait(2)
        self.play(tracker.animate.set_value(0.75),run_time = 8)
        self.wait(2)
        self.play(tracker.animate.set_value(0.999),run_time = 5)
        self.wait(2)
        self.play(tracker.animate.set_value(0),run_time = 10)
        self.play(tracker.animate.set_value(-0.75),run_time = 5)
        self.wait(1)
        self.play(tracker.animate.set_value(-0.999),run_time = 5)
        self.wait(1)
        self.play(tracker.animate.set_value(0),run_time = 10)
        self.wait(2)


        self.play(Uncreate(s),Uncreate(s_prime),Uncreate(text),Uncreate(beta),Uncreate(x),Uncreate(x_prime),Uncreate(y),Uncreate(y_prime))
        self.wait(1)
        

        self.play(Create(x_prime_initial))
        self.wait(2)
        self.play(ReplacementTransform(x_prime_initial.copy(),x_prime_2))
        self.wait(2)
        self.play(ReplacementTransform(x_prime_2,x_prime_3))
        self.wait(1)
        self.play(ReplacementTransform(x_prime_3,x_prime_rearrange))
        self.wait(1)
        self.play(ReplacementTransform(x_prime_rearrange[3:8].copy(),x_prime_rearrange_2))
        self.wait(1)
        self.play(ReplacementTransform(x_prime_rearrange_2,x_prime_rearrange_3))
        self.wait(1)



        self.play(Create(t_prime))
        self.wait(1)
        self.play(ReplacementTransform(t_prime.copy(),t_prime_2))
        self.wait(1)
        self.play(ReplacementTransform(t_prime_2,t_prime_3))
        self.wait(1)
        self.play(ReplacementTransform(t_prime_3,t_prime_4))
        self.wait(1)
        self.play(ReplacementTransform(t_prime_4.copy(),t_prime_5))
        self.wait(1)
        self.play(ReplacementTransform(t_prime_5,t_prime_6))

        self.play(Uncreate(x_prime_initial),Uncreate(x_prime_2),Uncreate(x_prime_3),Uncreate(x_prime_rearrange),Uncreate(x_prime_rearrange_2),Uncreate(x_prime_rearrange_3),Uncreate(t_prime),Uncreate(t_prime_2),Uncreate(t_prime_3),Uncreate(t_prime_4),Uncreate(t_prime_5))
        t_prime_6.generate_target()
        t_prime_6_moved = t_prime_6.copy().to_edge(UR).shift([0,-1.5,0])
        self.play(ReplacementTransform(t_prime_6,t_prime_6_moved))

        self.wait(1)



        y_prime = MathTex("ct'").set_color(GREEN)
        x_prime = MathTex("x'").set_color(GREEN)    
        
        y_prime.add_updater(lambda x: x.move_to(s_prime.coords_to_point(0,4.3)))
        x_prime.add_updater(lambda x: x.move_to(s_prime.coords_to_point(4.3,0)))


        s = NumberPlane(x_range = [-5,5],y_range = [-5,5]).shift([-2,0,0])
        beta = DecimalNumber(0,num_decimal_places= 3).to_corner(UR)
        beta.add_updater(lambda x: x.set_value(tracker.get_value()))
        self.play(Create(s),Create(s_prime),Create(text_2),Create(beta),Create(x),Create(y),Create(x_prime),Create(y_prime))

        y = MathTex("ct").move_to(s.coords_to_point(-0.5,3.85))
        x = MathTex("x").move_to(s.coords_to_point(5.1,0))
        self.add(s,s_prime,x,x_prime,y,y_prime)
        self.play(tracker.animate.set_value(0.5),run_time = 10)
        self.wait(2)

        one = MathTex("1").move_to(s.coords_to_point(1,0)).shift([0,-0.5,0])

        

        self.wait(2)

        self.play(Create(one))


        self.wait(1)
        
        self.play(Indicate(y),Indicate(t_prime_6_moved[0]),Indicate(one))

        
        tan = MathTex("tan(\\theta ) = \\beta ").move_to(t_prime_6_moved.get_center()).shift([-0.5,0,0])

        self.play(ReplacementTransform(t_prime_6_moved,tan))
        theta_text = MathTex("\\theta = ").move_to(tan.get_center()).shift([-1,-1,0])
        theta = DecimalNumber(0,num_decimal_places= 3).next_to(theta_text,RIGHT)
        theta.add_updater(lambda x: x.set_value(math.atan(tracker.get_value()) * (1/DEGREES)))
        self.wait(1)

        #self.play(Create(theta_text),Create(theta))
        
        self.play(ReplacementTransform(tan.copy(),theta_text),Create(theta))
        self.add(theta)

        


        
        



        self.play(tracker.animate.set_value(-0.5),run_time = 4)

        self.wait(2)
        
        self.play(tracker.animate.set_value(0),run_time = 4)

        

        
        