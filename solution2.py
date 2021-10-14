from manim import *
from code2 import nums
class Work(Scene):
    def construct(self):
        # 开场动画
        self.camera.background_color = WHITE
        banner = ManimBanner(dark_theme=False)
        self.play(banner.create())
        self.play(banner.expand())
        self.play(Unwrite(banner))

        color1 = GREY_C
        color2 = BLUE
        color3 = RED
        color4 = ORANGE



        py_code = Code("code2.py", tab_width=4, background="window",
                       language="Python",
                       style= "paraiso-light",
                       font="Consolas",
                       line_spacing=1
                       ).shift(RIGHT * 3 + UP*0.25).scale(0.8)
        codeline = py_code[1]
        codeline_distance = codeline[1].get_center() - codeline[0].get_center()  # 负数，方向向下
        for_n_y = codeline[1].get_y() #  代码for n in nums 的y坐标
        while_y = codeline[6].get_y() #  代码while l<=r 的y坐标
        self.add(py_code)


        # 箭头在第一行
        vector_code = Vector(RIGHT * 0.8, tip_length=0.2).shift(ORIGIN).set_color(color1).\
                             next_to(codeline[0], direction=LEFT, buff=0.1).scale(0.8)
        self.add(vector_code)
        vector_code_run_time = 1.5

        text1 = Text("nums", color=color1, font="Consolas", font_size=24).shift(LEFT * 6.5 + UP * 2)
        nums_matrix = IntegerMatrix([nums], h_buff=0.8).set_color(color1).scale(0.6).next_to(text1)
        nums_num = nums_matrix.get_columns()
        nums_vg = VGroup(text1, nums_matrix)
        num_distance = nums_num[1].get_center() - nums_num[0].get_center()
        self.play(Write(nums_vg))



        text2 = Text("d", color=color1, font="Consolas", font_size=24).shift(LEFT * 6.5 + UP)
        d_nums = ["*"] * len(nums)
        d_num_matrix = Matrix([d_nums], h_buff=0.8).\
                                set_color(color1).scale(0.6).\
                                next_to(text2, buff=0.55)
        d_nums_num = d_num_matrix[0]
        d_nums_vg = VGroup(text2, d_num_matrix)

        self.play(Write(d_nums_vg))



        # 箭头移动到第二行
        self.play(vector_code.animate.shift(codeline_distance), run_time=vector_code_run_time)


        # n索引
        n_Arrow = Arrow(UP*0.5, DOWN*0.5, tip_length=0.2).set_color(color2).next_to(nums_num[0], direction=UP, buff=0.2)
        n_text = Text("n", color=color2, font="Consolas", font_size=20). \
            next_to(n_Arrow, direction=RIGHT, buff=0.1)
        n_vg = VGroup(n_Arrow, n_text)
        self.play(FadeIn(n_vg))

        # l、r、loc、mid索引
        l_Arrow = Arrow(DOWN*0.4, UP*0.5, tip_length=0.2).set_color(color3).next_to(d_nums_num[0], direction=DOWN, buff=0.2)
        l_text = Text("l", color=color3, font="Consolas", font_size=20). \
            next_to(l_Arrow, direction=RIGHT, buff=0.1)
        l_vg = VGroup(l_Arrow, l_text)

        r_Arrow = Arrow(DOWN*0.4, UP*0.5, tip_length=0.2).set_color(color2).next_to(d_nums_num[0], direction=DOWN+[0, 0.1, 0], buff=0.2)
        r_text = Text("r", color=color2, font="Consolas", font_size=20). \
            next_to(r_Arrow, direction=RIGHT, buff=0.2)
        r_vg = VGroup(r_Arrow, r_text)

        loc_Arrow = Arrow(UP*0.4, DOWN*0.5, tip_length=0.2).set_color(color4).next_to(d_nums_num[0], direction=UP, buff=0.1)
        loc_text = Text("loc", color=color4, font="Consolas", font_size=20). \
            next_to(loc_Arrow, direction=RIGHT, buff=0.15)
        loc_vg = VGroup(loc_Arrow, loc_text)

        mid_Arrow = Arrow(DOWN * 0.5, UP * 0.4, tip_length=0.2).\
                    set_color(color4).next_to(d_nums_num[0], direction=DOWN,buff=0.8)
        mid_text = Text("mid", color=color4, font="Consolas", font_size=20). \
            next_to(mid_Arrow, direction=DOWN, buff=0.15)
        mid_vg = VGroup(mid_Arrow, mid_text)

        d = []
        count = 0
        for n in range(len(nums)):



            self.play(vector_code.animate.shift(codeline_distance), run_time=vector_code_run_time) # 箭头移动
            # if count > 0:
            #     self.play(Circumscribe(d_nums_num[count-1], color=BLUE_E), Circumscribe(nums_num[n], color=BLUE_E))
            if not d or nums[n] > d[-1]:


                self.play(vector_code.animate.shift(codeline_distance), run_time=vector_code_run_time) # 箭头移动


                temp1_tex = MathTex(str(nums[n]), color=color1).\
                    shift(d_nums_num[count].get_center()).scale(0.6)
                self.play(FadeOut(d_nums_num[count]), TransformFromCopy(nums_num[n], temp1_tex))
                d_nums_num[count] = temp1_tex

                self.play(vector_code.animate.move_to([vector_code.get_x(), for_n_y, 0])) # 箭头返回for_n
                d.append(nums[n])
                count = count + 1
            else:
                self.play(vector_code.animate.shift(3 * codeline_distance), run_time=vector_code_run_time) # 移到else下一行

                self.add(l_vg, r_vg, loc_vg)

                l, r = 0, len(d) - 1; loc = r

                self.play(
                    r_vg.animate.
                          move_to([d_nums_num[r].get_x() + r_vg.get_x() - r_vg[0].get_x(),
                                   r_vg.get_y(), 0]),
                    l_vg.animate.move_to([d_nums_num[l].get_x() + l_vg.get_x() - l_vg[0].get_x(),
                                       l_vg.get_y(), 0]),
                    loc_vg.animate.move_to([d_nums_num[loc].get_x() + loc_vg.get_x() - loc_vg[0].get_x(),
                                       loc_vg.get_y(), 0]),
                          run_time=vector_code_run_time)


                self.play(vector_code.animate.shift(1 * codeline_distance), run_time=vector_code_run_time)

                while l <= r:
                    self.play(vector_code.animate.shift(1 * codeline_distance), run_time=vector_code_run_time)
                    mid = (l + r) // 2

                    self.add(mid_vg)
                    self.play(mid_vg.animate.move_to([d_nums_num[mid].get_x(), mid_vg.get_y(), 0]))

                    self.play(vector_code.animate.shift(1 * codeline_distance), run_time=vector_code_run_time)
                    # self.play(Circumscribe(d_nums_num[mid], color=BLUE_E), Circumscribe(nums_num[n], color=BLUE_E))
                    if d[mid] >= nums[n]:


                        self.play(vector_code.animate.shift(1 * codeline_distance), run_time=vector_code_run_time)


                        loc = mid

                        self.play(loc_vg.animate.
                                  move_to([d_nums_num[loc].get_x() + loc_vg.get_x() - loc_vg[0].get_x(),
                                           loc_vg.get_y(), 0]), run_time=vector_code_run_time)


                        self.play(vector_code.animate.shift(codeline_distance), run_time=vector_code_run_time)
                        r = mid - 1
                        if r < 0:
                            self.play(r_vg.animate.
                                      shift(r*num_distance), run_time=vector_code_run_time)
                        else:
                            self.play(r_vg.animate.
                                  move_to([d_nums_num[r].get_x() + r_vg.get_x() - r_vg[0].get_x(),
                                           r_vg.get_y(), 0]), run_time=vector_code_run_time)

                        self.play(vector_code.animate.move_to([vector_code.get_x(), while_y, 0]))  # 箭头返回while
                    else:
                        self.play(vector_code.animate.shift(4 * codeline_distance),
                                  run_time=vector_code_run_time)  # 移到else下一行

                        l = mid + 1
                        self.play(l_vg.animate.
                                  move_to([d_nums_num[l].get_x() + l_vg.get_x() - l_vg[0].get_x(),
                                           l_vg.get_y(), 0]), run_time=vector_code_run_time)
                        self.play(vector_code.animate.move_to([vector_code.get_x(), while_y, 0]))  # 箭头返回while


                self.play(vector_code.animate.shift(7 * codeline_distance), run_time=vector_code_run_time) # 箭头移到d[loc] = n
                self.play(FadeOut(mid_vg), FadeOut(l_vg), FadeOut(r_vg), run_time=0.2)


                self.play(Circumscribe(d_nums_num[loc], color=BLUE_E))
                temp2_tex = MathTex(str(nums[n]), color=color1). \
                    shift(d_nums_num[loc].get_center()).scale(0.6)
                self.play(FadeOut(d_nums_num[loc]), TransformFromCopy(nums_num[n], temp2_tex))
                d_nums_num[loc] = temp2_tex
                d[loc] = n
                self.play(vector_code.animate.move_to([vector_code.get_x(), for_n_y, 0]))  # 箭头返回for_n

                self.play(vector_code.animate.move_to([vector_code.get_x(), for_n_y, 0]))  # 箭头返回for_n

            if n != len(nums) - 1:
                self.play(n_vg.animate.shift(num_distance), run_time=vector_code_run_time)  # 箭头移动
        ans = len(d)
        self.play(vector_code.animate.shift(13 * codeline_distance), run_time=vector_code_run_time)
        len_brace = BraceBetweenPoints(d_nums_num[0].get_center(), d_nums_num[count-1].get_center(), sharpness=0.8, color=color3)
        len_brace_text= Text("ans="+str(ans), color=color3, font="Consolas", font_size=20). \
            next_to(len_brace, direction=DOWN, buff=0.15)

        self.remove(loc_vg, l_vg, r_vg)
        self.play(FadeIn(len_brace))
        self.play(Write(len_brace_text))

        self.wait()

if __name__== "__main__":
    import os
    classname = 'Work'
    str = 'manim ' + '-pqk ' + str(__file__) + ' ' + classname

    os.system(str)