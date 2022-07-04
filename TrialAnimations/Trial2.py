from manim import *

class LinearTransformation(LinearTransformationScene):

    def construct(self):
        # self.Intro()
        matrix = [[1, 1], [0, 1]]
        self.apply_matrix(matrix)
        self.wait()

        matrix2 = [[1, 0], [0, 1]]
        self.apply_matrix(matrix2)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        # self.pappy()

    def pappy(self):
        formula = MathTex(r"[z^n]f(z) = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z^{n+1}}~dz")
        self.play(Write(formula), run_time=3)
        self.wait()

    def Intro(self):
        line1 = Text("So I wanted to make a video.....")
        line2 = Text("On a very interesting topic")
        line3 = Text("Something we all seek")
        line4 = Text("Love and Relationships")
        line5 = Text("lmao")
        line6 = Text("no")
        line7 = Text("baby steps guys")
        line8 = Text("\b{General Relativity}")
        formula = MathTex(r"[z^n]f(z) = \frac{1}{2\pi i}\oint_{\gamma} \frac{f(z)}{z^{n+1}}~dz")

        lines = [line1, line2, line3, line4, line5, line6, line7,line8, formula]

        [self.Showline(line) for line in lines]

    def Showline(self, line):
        self.play(Write(line))
        self.play(FadeOut(line))
