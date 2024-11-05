from manim import *

class DetailedGaussJordanElimination(Scene):
    def construct(self):
        # Initial system of equations
        system = MathTex(
            r"\begin{cases} 2x + y - z = 8 \\ -3x - y + 2z = -11 \\ -2x + y + 2z = -3 \end{cases}"
        ).scale(0.8)
        
        # Create initial augmented matrix
        matrix = MathTex(r"\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}").scale(0.8)
        
        # Show transition from system to matrix
        self.play(Write(system))
        self.wait()
        self.play(Transform(system, matrix))
        self.wait()

        # Step 1: Make first column's pivot 1
        calc1 = MathTex(
            r"\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}\\",
            r"\rightarrow_{\frac{1}{2}R_1}",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}"
        ).scale(0.7)
        
        self.play(Transform(system, calc1))
        self.wait()

        # Step 2: Eliminate below first pivot - Row 2
        calc2 = MathTex(
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}\\",
            r"\rightarrow_{3\times R_1 + R_2}",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}"
        ).scale(0.7)
        
        calc2_detail = MathTex(
            r"3(1)+(-3) & = 0 \\",
            r"3\cdot\frac{1}{2}+(-1) & = \frac{1}{2} \\",
            r"3\cdot(-\frac{1}{2}) + 2  & = \frac{1}{2} \\",
            r"3\cdot4 + (-11)  & = 1"
        ).scale(0.6)
        calc2_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc2))
        self.play(Write(calc2_detail))
        self.wait(2)
        self.play(FadeOut(calc2_detail))

        # Step 3: Eliminate below first pivot - Row 3
        calc3 = MathTex(
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}\\",
            r"\rightarrow_{2\times R_1 + R_3}",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}"
        ).scale(0.7)
        
        calc3_detail = MathTex(
            r"2(1) + (-2) & = 0 \\",
            r"2\cdot\frac{1}{2} + 1 & = 2 \\",
            r"2\cdot(-\frac{1}{2}) + 2 & = 1 \\",
            r"2\cdot4 + (-3)  & = 5"
        ).scale(0.6)
        calc3_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc3))
        self.play(Write(calc3_detail))
        self.wait(2)
        self.play(FadeOut(calc3_detail))

        # Step 4: Make second pivot 1
        calc4 = MathTex(
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}\\",
            r"\rightarrow_{2\times R_2}",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}"
        ).scale(0.7)
        
        self.play(Transform(system, calc4))
        self.wait()

        # Step 5a: Eliminate above second pivot
        calc5a = MathTex(
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}\\",
            r"\rightarrow_{-\frac{1}{2}\times R_2 + R_1}",
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}"
        ).scale(0.7)
        
        calc5a_detail = MathTex(
            r"0 + 0 & = 0\\",
            r"- \frac{1}{2}\cdot1 + \frac{1}{2} & = 0 \\",
            r"-\frac{1}{2}\cdot1 + (-\frac{1}{2}) & = -1 \\",
            r"- \frac{1}{2}\cdot2 + 4  & = 3 \\",
        ).scale(0.6)
        calc5a_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc5a))
        self.play(Write(calc5a_detail))
        self.wait(2)
        self.play(FadeOut(calc5a_detail))

        # Step 5b: Eliminate below second pivot

        calc5b = MathTex(
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}\\",
            r"\rightarrow_{-2\times R_2 + R_3}",
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & -1 & | & 1 \end{bmatrix}"
        ).scale(0.7)

        calc5b_detail = MathTex(
            r"0 + 0 & = 0\\",
            r"- 2\cdot1 + 2 & = 0 \\",
            r"- 2\cdot1 + 1 & = -1 \\",
            r"- 2\cdot2 + 5 & = 1"
        ).scale(0.6)
        calc5b_detail.to_edge(RIGHT)

        self.play(Transform(system, calc5b))
        self.play(Write(calc5b_detail))
        self.wait(2)
        self.play(FadeOut(calc5b_detail))

        # Step 6a: Make last pivot 1
        calc6a = MathTex(
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & -1 & | & 1 \end{bmatrix}\\",
            r"\rightarrow_{-1\times R_3}",
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}"
        ).scale(0.7)

        self.play(Transform(system,calc6a))
        self.wait()
        
        # Step 6b: Eliminate above the last pivot r1

        calc6b = MathTex(
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}\\",
            r"\rightarrow_{R_3 + R_1}",
            r"\begin{bmatrix} 1 & 0 & 0 & | & 2 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}"
        ).scale(0.7)

        calc6b_detail = MathTex(
            r"0 + 1 & = 1 \\",
            r"0 + 0 & = 0 \\",
            r"1 + (-1) & = 0 \\",
            r"-1 + 3 & = 2"
        ).scale(0.6)
        calc6b_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc6b))
        self.play(Write(calc6b_detail))
        self.wait(2)
        self.play(FadeOut(calc6b_detail))

        # Step 6c: Eliminate above the last pivot r2

        calc6c = MathTex(
            r"\begin{bmatrix} 1 & 0 & 0 & | & 2 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}\\",
            r"\rightarrow_{-1\times R_3 + R_2}",
            r"\begin{bmatrix} 1 & 0 & 0 & | & 2 \\ 0 & 1 & 0 & | & 3 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}"
        ).scale(0.7)

        calc6c_detail = MathTex(
            r"0+0 & = 0\\",
            r"0+1 & = 1\\",
            r"-1 + 1 & = 0\\",
            r"-1\cdot (-1) + 2 & = 3"
        ).scale(0.7)
        calc6c_detail.to_edge(RIGHT)

        self.play(Transform(system, calc6c))
        self.play(Write(calc6c_detail))
        self.wait(2)
        self.play(FadeOut(calc6c_detail))

        # Show final solution
        solution = MathTex(
            r"\begin{cases} x = 2 \\ y = 3 \\ z = -1 \end{cases}"
        ).scale(0.8)
        
        self.play(Transform(system, solution))
        self.wait(2)
