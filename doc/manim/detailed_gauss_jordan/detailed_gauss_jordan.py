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
            r"R_1 \rightarrow \frac{1}{2}R_1:",
            r"\begin{bmatrix} 2 & 1 & -1 & | & 8 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}",
            r"\rightarrow",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}"
        ).scale(0.7)
        
        self.play(Transform(system, calc1))
        self.wait()

        # Step 2: Eliminate below first pivot - Row 2
        calc2 = MathTex(
            r"R_2 \rightarrow R_2 + 3R_1:",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ -3 & -1 & 2 & | & -11 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}",
            r"\rightarrow",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}"
        ).scale(0.7)
        
        calc2_detail = MathTex(
            r"R_2: (-3 + 3) & = 0 \\",
            r"(-1 + 3\cdot\frac{1}{2}) & = \frac{1}{2} \\",
            r"(2 + 3\cdot(-\frac{1}{2})) & = \frac{1}{2} \\",
            r"(-11 + 3\cdot4) & = 1"
        ).scale(0.6)
        calc2_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc2))
        self.play(Write(calc2_detail))
        self.wait()
        self.play(FadeOut(calc2_detail))

        # Step 3: Eliminate below first pivot - Row 3
        calc3 = MathTex(
            r"R_3 \rightarrow R_3 + 2R_1:",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ -2 & 1 & 2 & | & -3 \end{bmatrix}",
            r"\rightarrow",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}"
        ).scale(0.7)
        
        calc3_detail = MathTex(
            r"R_3: (-2 + 2) & = 0 \\",
            r"(1 + 2\cdot\frac{1}{2}) & = 2 \\",
            r"(2 + 2\cdot(-\frac{1}{2})) & = 1 \\",
            r"(-3 + 2\cdot4) & = 5"
        ).scale(0.6)
        calc3_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc3))
        self.play(Write(calc3_detail))
        self.wait()
        self.play(FadeOut(calc3_detail))

        # Step 4: Make second pivot 1
        calc4 = MathTex(
            r"R_2 \rightarrow 2R_2:",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & \frac{1}{2} & \frac{1}{2} & | & 1 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}",
            r"\rightarrow",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}"
        ).scale(0.7)
        
        self.play(Transform(system, calc4))
        self.wait()

        # Step 5: Eliminate above and below second pivot
        calc5 = MathTex(
            r"R_1 \rightarrow R_1 - \frac{1}{2}R_2, R_3 \rightarrow R_3 - 2R_2:",
            r"\begin{bmatrix} 1 & \frac{1}{2} & -\frac{1}{2} & | & 4 \\ 0 & 1 & 1 & | & 2 \\ 0 & 2 & 1 & | & 5 \end{bmatrix}",
            r"\rightarrow",
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & -1 & | & 1 \end{bmatrix}"
        ).scale(0.7)
        
        calc5_detail = MathTex(
            r"R_1: (\frac{1}{2} - \frac{1}{2}\cdot1) & = 0 \\",
            r"(-\frac{1}{2} - \frac{1}{2}\cdot1) & = -1 \\",
            r"(4 - \frac{1}{2}\cdot2) & = 3 \\",
            r"R_3: (2 - 2\cdot1) & = 0 \\",
            r"(1 - 2\cdot1) & = -1 \\",
            r"(5 - 2\cdot2) & = 1"
        ).scale(0.6)
        calc5_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc5))
        self.play(Write(calc5_detail))
        self.wait()
        self.play(FadeOut(calc5_detail))

        # Step 6: Make last pivot 1 and eliminate above
        calc6 = MathTex(
            r"R_3 \rightarrow -R_3, \text{ then } R_1 \rightarrow R_1 + R_3:",
            r"\begin{bmatrix} 1 & 0 & -1 & | & 3 \\ 0 & 1 & 1 & | & 2 \\ 0 & 0 & -1 & | & 1 \end{bmatrix}",
            r"\rightarrow",
            r"\begin{bmatrix} 1 & 0 & 0 & | & 2 \\ 0 & 1 & 0 & | & 1 \\ 0 & 0 & 1 & | & -1 \end{bmatrix}"
        ).scale(0.7)
        
        calc6_detail = MathTex(
            r"\text{First: } R_3 \rightarrow -R_3 \\",
            r"\text{Then: } R_1: (1 + 0) & = 1 \\",
            r"(0 + 0) & = 0 \\",
            r"(-1 + 1) & = 0 \\",
            r"(3 + (-1)) & = 2"
        ).scale(0.6)
        calc6_detail.to_edge(RIGHT)
        
        self.play(Transform(system, calc6))
        self.play(Write(calc6_detail))
        self.wait()
        self.play(FadeOut(calc6_detail))

        # Show final solution
        solution = MathTex(
            r"\begin{cases} x = 2 \\ y = 1 \\ z = -1 \end{cases}"
        ).scale(0.8)
        
        self.play(Transform(system, solution))
        self.wait(2)

class ExplanationText(Scene):
    def construct(self):
        explanation = VGroup(
            Text("Key Steps in Gauss-Jordan Elimination:", weight=BOLD).scale(0.8),
            Text("1. Convert system to augmented matrix").scale(0.6),
            Text("2. Make leading coefficient (pivot) in first column = 1").scale(0.6),
            Text("3. Create zeros below pivot using row operations").scale(0.6),
            Text("4. Repeat for second column").scale(0.6),
            Text("5. Make last pivot = 1").scale(0.6),
            Text("6. Create zeros above pivots").scale(0.6),
            Text("7. Read solution from last column").scale(0.6)
        ).arrange(DOWN, aligned_edge=LEFT)
        
        explanation[0].to_edge(UP)
        for i in range(1, len(explanation)):
            explanation[i].next_to(explanation[i-1], DOWN, aligned_edge=LEFT)
            self.play(Write(explanation[i]))
            self.wait(0.5)
        
        self.wait(2)
