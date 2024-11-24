from manim import *

class CoolAnimation(Scene):
	def construct(self):
		rect1 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		rect2 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1).move_to([5, 0, 0])
		
		r1 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r2 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r3 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r4 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r5 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		
		g = VGroup(r1, r2, r3, r4, r5)
		g.arrange()
		g.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN)
		
		self.wait(1)
		
		self.play(Write(rect1))
		self.play(Write(rect2))
		
		self.play(rect1.animate.shift(LEFT * 5))
		self.play(rect2.animate.next_to(rect1, RIGHT))
		
		g2 = VGroup(rect1, rect2)
		
		self.play(ReplacementTransform(g2, g))
		
		s1 = SurroundingRectangle(g, color = WHITE)
		s2 = SurroundingRectangle(s1, color = WHITE)
		
		self.play(Write(s1), Write(s2, run_time = 1.5))
		
		num1 = Text("1")
		num1_2 = Text("1")
		num2 = Text("2")
		num3 = Text("3")
		num4 = Text("4")
		num5 = Text("5")
		
		numGroup = VGroup(num1_2, num2, num3, num4, num5)
		
		numGroup.scale(1.5)
		num1_2.scale(1.2)
		num2.scale(1.2)
		num1.scale(2)
		num1.shift(LEFT * 5)
		
		sLines = VGroup(s1, s2)
		
		numGroup.arrange()
		
		self.play(g.animate.move_to([0, 1, 0]), g2.animate.move_to([0, 1, 0]), sLines.animate.move_to([0, 1, 0]))
		self.play(Write(num1), run_time = 2)
		self.play(ReplacementTransform(num1, numGroup))
		self.play(g.animate.move_to([0, 0, 0]), g2.animate.move_to([0, 0, 0]), sLines.animate.move_to([0, 0, 0]), numGroup.animate.move_to([0, 1, 0]))
		
		self.play(Indicate(num1_2, color = RED), Indicate(r1, color = RED), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num2, color = ORANGE), Indicate(r2, color = ORANGE), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num3, color = g[2].get_color()), Indicate(r3, color = g[2].get_color()), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num4, color = g[3].get_color()), Indicate(r4, color = g[3].get_color()), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num5, color = PURE_GREEN), Indicate(r5, color = PURE_GREEN), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		
		dot = Dot(color = RED)
		
		allObjs = VGroup(numGroup, g, g2, sLines)
		
		self.play(ReplacementTransform(allObjs, dot))
		
		self.play(dot.animate.scale(150))
		self.play(FadeOut(dot))
		
		self.wait(1)
		
		letterM = Text("M")
		meuPau = Text("Meu Pau")
		
		letterM.shift(LEFT * 5)
		
		self.play(Write(letterM))
		
		self.play(ReplacementTransform(letterM, meuPau))
		
		self.wait(1)
		self.play(meuPau.animate.scale(1000), run_time = 3)
		
class CoolAnimationNoMeuPau(Scene):
	def construct(self):
		rect1 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		rect2 = Rectangle(height = 0.5, width = 0.5, fill_opacity = 1).move_to([5, 0, 0])
		
		r1 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r2 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r3 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r4 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		r5 =  Rectangle(height = 0.5, width = 0.5, fill_opacity = 1)
		
		g = VGroup(r1, r2, r3, r4, r5)
		g.arrange()
		g.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN)
		
		self.wait(1)
		
		self.play(Write(rect1))
		self.play(Write(rect2))
		
		self.play(rect1.animate.shift(LEFT * 5))
		self.play(rect2.animate.next_to(rect1, RIGHT))
		
		g2 = VGroup(rect1, rect2)
		
		self.play(ReplacementTransform(g2, g))
		
		s1 = SurroundingRectangle(g, color = WHITE)
		s2 = SurroundingRectangle(s1, color = WHITE)
		
		self.play(Write(s1), Write(s2, run_time = 1.5))
		
		num1 = Text("1")
		num1_2 = Text("1")
		num2 = Text("2")
		num3 = Text("3")
		num4 = Text("4")
		num5 = Text("5")
		
		numGroup = VGroup(num1_2, num2, num3, num4, num5)
		
		numGroup.scale(1.5)
		num1_2.scale(1.2)
		num2.scale(1.2)
		num1.scale(2)
		num1.shift(LEFT * 5)
		
		sLines = VGroup(s1, s2)
		
		numGroup.arrange()
		
		self.play(g.animate.move_to([0, 1, 0]), g2.animate.move_to([0, 1, 0]), sLines.animate.move_to([0, 1, 0]))
		self.play(Write(num1), run_time = 2)
		self.play(ReplacementTransform(num1, numGroup))
		self.play(g.animate.move_to([0, 0, 0]), g2.animate.move_to([0, 0, 0]), sLines.animate.move_to([0, 0, 0]), numGroup.animate.move_to([0, 1, 0]))
		
		self.play(Indicate(num1_2, color = RED), Indicate(r1, color = RED), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num2, color = ORANGE), Indicate(r2, color = ORANGE), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num3, color = g[2].get_color()), Indicate(r3, color = g[2].get_color()), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num4, color = g[3].get_color()), Indicate(r4, color = g[3].get_color()), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		self.play(Indicate(num5, color = PURE_GREEN), Indicate(r5, color = PURE_GREEN), Indicate(sLines, color = WHITE, scale_factor = 1.05))
		
		dot = Dot(color = RED)
		
		allObjs = VGroup(numGroup, g, g2, sLines)
		
		self.play(ReplacementTransform(allObjs, dot))
		
		self.play(dot.animate.scale(150))
		self.play(FadeOut(dot))