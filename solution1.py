from manim import *
from code1 import nums
class Work(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        # plane = NumberPlane()
        # self.add(plane)
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.wait()
        self.play(Unwrite(banner))


        color1 = GREY_C
        color2 = GREY_C
        color3 = BLUE
        color4 = RED


        text1 = Text("nums", color=color2, font="Consolas", font_size=24).shift(LEFT * 4 + DOWN * 0.5)
        nums_matrix = IntegerMatrix([nums], h_buff=1.5).set_color(color2).scale(0.6).next_to(text1)
        nums_num = nums_matrix.get_columns()
        nums_vg = VGroup(text1, nums_matrix)


        # 调试用
        # for i in nums_matrix.get_columns():
        #     dot = Dot(point=LEFT, radius=0.08, color=BLACK).next_to(i, direction=DOWN, buff=0.1)
        #     self.add(dot)

        text2 = Text("dp", color=color2, font="Consolas", font_size=24).\
                            shift(LEFT * 4 + DOWN * 0.5).\
                            next_to(text1, direction=DOWN, buff=1.3)
        dp_nums = [0] * (len(nums))
        dp_num_matrix = IntegerMatrix([dp_nums], h_buff=1.5).\
                                set_color(color2).scale(0.6).\
                                next_to(nums_matrix, direction=DOWN, buff=1)
        dp_nums_num = dp_num_matrix.get_columns()
        dp_nums_vg = VGroup(text2, dp_num_matrix)




        py_code = Code("code1.py", tab_width=4, background="window",
                       language="Python",
                       style= "paraiso-light",
                       font="Consolas",
                       line_spacing=1
                       ).shift(RIGHT * 3 + UP*2.2).scale(0.8)
        codeline = py_code[1]
        self.add(py_code)


        # 箭头在第一行
        vector1_run_time = 1
        vector1 = Vector(RIGHT).shift(ORIGIN).set_color(color2).\
                             next_to(codeline[0], direction=LEFT, buff=0.2).scale(1)
        self.add(vector1)
        self.play(Write(nums_vg), Write(dp_nums_vg))
        self.wait(vector1_run_time)

        # 箭头移动到第二行
        line_distance = codeline[2].get_center() - codeline[1].get_center()
        self.play(vector1.animate.
                  shift(line_distance), run_time=vector1_run_time)
        i_doubleArrow = DoubleArrow(UP*0.5, DOWN, tip_length=0.1).set_color(color3).next_to(dp_nums_num[0], direction=UP, buff=0.1)
        i_text = Text("i", color=color3, font="Consolas", font_size=24).\
                    next_to(i_doubleArrow, direction=RIGHT, buff=0.1)
        i_vg = VGroup(i_doubleArrow, i_text)
        self.add(i_vg)




        num_distance = dp_nums_num[1].get_center() - dp_nums_num[0].get_center()
        num_start = dp_nums_num[0].get_center()
        j_doubleArrow = DoubleArrow(UP*0.5, DOWN*0.5, tip_length=0.1).set_color(color4).next_to(dp_nums_num[0], direction=UP, buff=0.4)
        j_text = Text("j", color=color4, font="Consolas", font_size=20). \
            next_to(j_doubleArrow, direction=RIGHT, buff=0.1)
        j_vg = VGroup(j_doubleArrow, j_text)
        self.wait(vector1_run_time)

        dp = []
        for i in range(len(nums)):
            dp.append(1)
            self.play(vector1.animate.
                      shift(line_distance), run_time=vector1_run_time)

            temp1_text = MathTex("1", color=color2).\
                    shift(dp_nums_num[i].get_center()).scale(0.6)

            self.play(Circumscribe(dp_nums_num[i], color=BLUE_E))
            self.play(FadeOut(dp_nums_num[i]), run_time=0.1)
            self.play(FadeIn(temp1_text))
            dp_nums_num[i] = temp1_text

            self.play(vector1.animate.
                          shift(line_distance), run_time=vector1_run_time)
            self.add(j_vg)
            self.play(j_vg.animate.shift(-max(0,(i - 1)) * num_distance))

            for j in range(i):

                self.play(vector1.animate.
                          shift(line_distance), run_time=vector1_run_time)


                if nums[i] > nums[j]:
                    self.play(vector1.animate.
                              shift(line_distance), run_time=vector1_run_time)



                    dp[i] =  max(dp[i], dp[j] + 1)
                    temp2_text = MathTex(str(dp[i]), color=color2). \
                        shift(dp_nums_num[i].get_center()).scale(0.6)
                    self.play(Circumscribe(dp_nums_num[i], color=BLUE_E))
                    self.play(FadeOut(dp_nums_num[i]), run_time=0.1)
                    self.play(FadeIn(temp2_text))
                    dp_nums_num[i] = temp2_text


                self.play(vector1.animate.move_to([vector1.get_x(), codeline[3].get_y(), 0])) # 回到for j
                self.play(j_vg.animate.shift(num_distance))


            self.play(vector1.animate.move_to([vector1.get_x(), codeline[1].get_y(), 0])) # 回到上面for i
            if i!=len(nums)-1:
                self.play(i_vg.animate.shift(num_distance))

        self.play(vector1.animate.
                  shift(5 * line_distance), run_time=vector1_run_time)
        ans_Text = Text("ans", color=color4, font="Consolas", font_size=18). \
            next_to(dp_nums_num[-1], direction=DOWN, buff=0.2)
        self.remove(i_vg, j_vg)
        self.wait()
        self.add(ans_Text)
        self.play(Flash(dp_nums_num[-1], color=color4, flash_radius=0.3))
        self.wait(3)

if __name__== "__main__":
    import os
    classname = 'Work'
    str = 'manim ' + '-pqk ' + str(__file__) + ' ' + classname
    os.system(str)