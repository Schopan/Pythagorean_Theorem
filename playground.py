from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Create right-angled triangle
        triangle = Polygon(
            ORIGIN, RIGHT*2, UP*1.5, 
            color=WHITE, fill_color=BLUE, fill_opacity=0.5
        )
        hypotenuse = Line(RIGHT*2, UP*1.5, color=WHITE)
        
        # Add labels for sides
        a_label = MathTex("a").next_to(triangle.get_left(), LEFT)
        b_label = MathTex("b").next_to(triangle.get_bottom(), DOWN)
        c_label = MathTex("c").next_to(hypotenuse, UP, buff=0.2)

        # Create squares on each side
        # Square on side 'a'
        square_a = Polygon(
            ORIGIN, UP*1.5, UP*1.5 + LEFT*1.5, LEFT*1.5,
            color=GREEN, fill_color=GREEN, fill_opacity=0.5
        )
        a_sq_label = MathTex("a^2").move_to(square_a)

        # Square on side 'b'
        square_b = Polygon(
            ORIGIN, RIGHT*2, RIGHT*2 + DOWN*2, DOWN*2,
            color=RED, fill_color=RED, fill_opacity=0.5
        )
        b_sq_label = MathTex("b^2").move_to(square_b)

        # Square on hypotenuse 'c'
        hypo_square = Polygon(
            RIGHT*2, UP*1.5, UP*1.5 + RIGHT*1.5 + UP*2, RIGHT*2 + RIGHT*1.5 + UP*2,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.5
        )
        c_sq_label = MathTex("c^2").move_to(hypo_square)

        # Pythagorean theorem equation
        equation = MathTex("a^2", "+", "b^2", "=", "c^2") \
            .scale(1.5) \
            .to_edge(UP)

        # Animation sequence
        self.play(Create(triangle))
        self.wait()
        
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait()

        # Animate squares
        self.play(
            Create(square_a),
            Write(a_sq_label),
            run_time=2
        )
        self.wait()

        self.play(
            Create(square_b),
            Write(b_sq_label),
            run_time=2
        )
        self.wait()

        self.play(
            Create(hypo_square),
            Write(c_sq_label),
            run_time=2
        )
        self.wait()

        # Show equation
        self.play(Write(equation))
        self.wait()

        # Connect squares to equation
        self.play(
            a_sq_label.animate.move_to(equation[0]),
            b_sq_label.animate.move_to(equation[2]),
            c_sq_label.animate.move_to(equation[4]),
            run_time=2
        )
        self.wait(3)