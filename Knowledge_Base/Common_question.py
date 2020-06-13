from experta import *

class Common_Criteria(KnowledgeEngine):
    # common question to determine which choices to be shown
    weight_sci = 0
    weight_tech = 0
    weight_eng = 0
    weight_math = 0

    @DefFacts()
    def _initial_action(self):
        print("\nHere are some common question to determine "
              "which two branches among STEM will you be "
              "tested later. Please answer '1' or '2' based "
              "on the question given.")
        yield Fact()
        yield Fact(cm5='Working with puzzles and problem solving '
                       'or Learning from existing knowledge resources')
        yield Fact(cm4='learn theoretical knowledge or skills?')
        yield Fact(cm3='Working with words or numbers?')
        yield Fact(cm2='Working alone or in group?')
        yield Fact(cm1='Exploring theory or Solving problem?')

    # --------------------------------------------------
    # common question 1: study theory or solving problem
    @Rule(Fact(cm1='Exploring theory or Solving problem?'),
          NOT(Fact(respond_common_qs1=W())))
    def ask_cm1(self):
        print("Which one do you prefer?\n"
              "1. Exploring theory\n"
              "2. Solving problem\n")
        self.declare(Fact(respond_common_qs1=input()))

    # cm1 : exploring theory, add math, science
    @Rule(Fact(cm1='Exploring theory or Solving problem?'),
          Fact(respond_common_qs1='1'))
    def common_1_ans_1(self):
        self.weight_math += 1
        self.weight_sci += 1

    # cm1 : solving problem, add math, tech, eng
    @Rule(Fact(cm1='Exploring theory or Solving problem?'),
          Fact(respond_common_qs1='2'))
    def common_1_ans_2(self):
        self.weight_math += 1
        self.weight_tech += 1
        self.weight_eng += 1

    # -----------------------------------------
    # common question 2: work alone or in group
    @Rule(Fact(cm2='Working alone or in group?'),
          NOT(Fact(respond_common_qs2=W())))
    def ask_cm2(self):
        print("When you are studying or working, you prefer... "
              "(either 1 or 2)\n"
              "1. Work alone\n"
              "2. Working in group\n")
        self.declare(Fact(respond_common_qs2=input()))

    # cm2: work alone, add math, tech个人觉得tech在两边啦，讨论一下
    @Rule(Fact(cm2='Working alone or in group?'),
          Fact(respond_common_qs2='1'))
    def com2_ans_1(self):
        self.weight_math += 1
        self.weight_tech += 1

    # cm2 : work in group, add sci, eng, tech
    @Rule(Fact(cm2='Working alone or in group?'),
          Fact(respond_common_qs2='2'))
    def com2_ans_2(self):
        self.weight_sci += 1
        self.weight_tech += 1
        self.weight_eng += 1

    # --------------------------------------------------
    # common question 3: word or number
    @Rule(Fact(cm3='Working with words or numbers?'),
          NOT(Fact(respond_common_qs3=W())))
    def ask_cm3(self):
        print("During working/studying, you prefer to working "
              "more on words or numbers? (either 1 or 2)\n"
              "1. Words\n"
              "2. Numbers\n")
        self.declare(Fact(respond_common_qs3=input()))

    # cm3 : word, add sci, tech
    @Rule(Fact(cm3='Working with words or numbers?'),
          Fact(respond_common_qs3='1'))
    def com3_ans_1(self):
        self.weight_tech += 1
        self.weight_sci += 1

    # cm3 : number, add eng, math
    @Rule(Fact(cm3='Working with words or numbers?'),
          Fact(respond_common_qs3='2'))
    def com3_ans_2(self):
        self.weight_eng += 1
        self.weight_math += 1

    # --------------------------------------------------
    # common question 4: learn theoretical knowledge or skills
    @Rule(Fact(cm4='learn theoretical knowledge or skills?'),
          NOT(Fact(respond_common_qs4=W())))
    def ask_cm4(self):
        print("Do you prefer to learn... \n"
              "1. Theoretical Knowledge\n"
              "2. Skills\n")
        self.declare(Fact(respond_common_qs4=input()))

    # cm4 : theoretical knowledge, add sci, math
    @Rule(Fact(cm4='learn theoretical knowledge or skills?'),
          Fact(respond_common_qs4='1'))
    def com4_ans_1(self):
        self.weight_sci += 1
        self.weight_math += 1

    # cm4 : skill, add tech, eng
    @Rule(Fact(cm4='learn theoretical knowledge or skills?'),
          Fact(respond_common_qs4='2'))
    def com4_ans_2(self):
        self.weight_tech += 1
        self.weight_eng += 1

    # --------------------------------------------------
    # common question 5
    @Rule(Fact(cm5='Working with puzzles and problem solving '
                   'or Learning from existing knowledge resources'),
          NOT(Fact(respond_common_qs5=W())))
    def ask_cm5(self):
        print("Among the two activities below, what you think is more enjoyable?\n"
              "\t1. Working with puzzles and problem solving\n"
              "\t2. Learning from existing knowledge resources(ie books, videos, teachers)\n")
        self.declare(Fact(respond_common_qs5=input()))

    # cm5 : Working with puzzles and problem solving, add eng, math
    @Rule(Fact(cm5='Working with puzzles and problem solving '
                   'or Learning from existing knowledge resources'),
          Fact(respond_common_qs5='1'))
    def com5_ans_1(self):
        self.weight_eng += 1
        self.weight_math += 1

    # cm5 : Learning from existing knowledge resources, add sci, tech
    @Rule(Fact(cm5='Working with puzzles and problem solving '
                   'or Learning from existing knowledge resources'),
          Fact(respond_common_qs5='2'))
    def com5_ans_2(self):
        self.weight_sci += 1
        self.weight_tech += 1

    def collection(self):
        return [self.weight_sci, self.weight_tech, self.weight_eng, self.weight_math]
