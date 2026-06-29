from manim import *


class IrrationalRoot2(Scene):
    def construct(self):
        title = Tex(r"Proof that $\sqrt{2}$ is Irrational", font_size=52)

        step1 = Tex(
            r"Assume $\sqrt{2}$ is rational.",
            font_size=40,
        )

        step2 = Tex(
            r"Then $\sqrt{2}=\frac{a}{b}$, where $a,b\in\mathbb{Z}$ and the ratio is in simplest form.",
            font_size=36,
        )

        step3 = Tex(
            r"Squaring both sides gives: $2=\frac{a^2}{b^2}$.",
            font_size=40,
        )

        step4 = MathTex(r"2b^2=a^2", font_size=50)

        step5 = Tex(
            r"From $2b^2=a^2$, we see that $a^2$ is even.",
            font_size=40,
        )

        step6 = Tex(
            r"If $a^2$ is even, then $a$ is even.",
            font_size=40,
        )

        step7 = MathTex(r"a=2k\quad\text{for some }k\in\mathbb{Z}", font_size=46)

        step8 = MathTex(
            r"2b^2=(2k)^2=4k^2\Rightarrow b^2=2k^2",
            font_size=44,
        )

        step9 = Tex(
            r"So $b^2$ is even, hence $b$ is even.",
            font_size=40,
        )

        step10 = Tex(
            r"Then both $a$ and $b$ are even, contradicting that $\frac{a}{b}$ is in simplest form.",
            font_size=38,
        )

        conclusion = Tex(r"Therefore, our assumption is false, and $\sqrt{2}$ is irrational.", font_size=42, color=YELLOW)

        final_message = Text(
            "Careful with this information. It could get you killed.",
            font_size=36,
            color=RED,
        )

        final_subtitle = Text(
            "- Hippasus of Metapontum (legend)",
            font_size=26,
            color=GRAY_B,
        )

        self.play(Write(title), run_time=1.8)
        self.wait(1.0)
        self.play(FadeOut(title), run_time=0.8)

        steps = [step1, step2, step3, step4, step5, step6, step7, step8, step9, step10, conclusion]

        for step in steps:
            step.move_to(ORIGIN)
            self.play(Write(step), run_time=1.6)
            
            if step != step8:
                self.wait(1.0)
            else:
                self.wait(2.0)
                
            if step is not conclusion:
                self.play(FadeOut(step), run_time=0.7)

        self.play(FadeOut(conclusion), run_time=0.8)
        final_message.move_to(ORIGIN)
        final_subtitle.next_to(final_message, DOWN, buff=0.35)
        self.play(Write(final_message), run_time=1.8)
        self.play(FadeIn(final_subtitle), run_time=1.0)
        self.wait(1.2)


# To render this scene:
# manim -pql Manim-Irrational-Root2.py IrrationalRoot2
