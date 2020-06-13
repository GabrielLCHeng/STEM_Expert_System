from experta import *

class Mathematics_Related(KnowledgeEngine):
    mathematics_weight = 0
    total_question = 7

    @DefFacts()
    def initial_fact(self):
        print("Now STEM ES directs you to " + "\033[1m" + "Mathematics related" + "\033[0m"
              + " session. \nPlease answer 'yes' or 'no' based on the questions given.\n")
        yield Fact(action1='Some silly info related to Mathematics field')
        yield Fact(f7='Interested in Discrete Mathematics.')
        yield Fact(f6='Interested in Mathematical logic.')
        yield Fact(f5='Interested in Calculus.')
        yield Fact(f4='Interested in Geometry.')
        yield Fact(f3='Interested in Algebra.')
        yield Fact(f2='May have good mental calculation.')
        yield Fact(f1='Interested in Arithmetic.')

    # ---------------------------------------
    @Rule(Fact(f1='Interested in Arithmetic.'),
          NOT(Fact(respond_f1=W())))
    def f1(self):
        resp = input("Are you interested in Arithmetic?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f1='yes'))
            self.mathematics_weight += 1

    # ---------------------------------------
    @Rule(Fact(f2='May have good mental calculation.'),
          NOT(Fact(respond_f2=W())))
    def f2(self):
        resp = input("Do you have good mental calculation?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f2='yes'))
            self.mathematics_weight += 1

    # ---------------------------------------
    @Rule(Fact(f3='Interested in Algebra.'),
          NOT(Fact(respond_f3=W())))
    def f3(self):
        resp = input("Are interested in Algebra?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f3='yes'))
            self.mathematics_weight += 1

    # ---------------------------------------
    @Rule(Fact(f4='Interested in Geometry.'),
          NOT(Fact(respond_f4=W())))
    def f4(self):
        resp = input("Are you interested in Geometry?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f4='yes'))
            self.mathematics_weight += 1

    # ---------------------------------------
    @Rule(Fact(f5='Interested in Calculus.'),
          NOT(Fact(respond_f5=W())))
    def f5(self):
        resp = input("Are you interested in Calculus?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f5='yes'))
            self.mathematics_weight += 1

    # ---------------------------------------
    @Rule(Fact(f6='Interested in Mathematical logic.'),
          NOT(Fact(respond_f6=W())))
    def f6(self):
        resp = input("Are you interested in Mathematical Logic?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f6='yes'))
            self.mathematics_weight += 1

    # ---------------------------------------
    @Rule(Fact(f7='Interested in Discrete Mathematics.'),
          NOT(Fact(respond_f7=W())))
    def f7(self):
        resp = input("Are you interested in Discrete Mathematics?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f7='yes'))
            self.mathematics_weight += 1
    # ---------------------------------------

    def show_mathematics_mark(self):
        mark = int((self.mathematics_weight / self.total_question) * 100)
        print(f"You answered {self.total_question} questions in this 'Mathematics related' session.\n"
              f"You answered 'Yes' for {self.mathematics_weight} questions.\n"
              f"You get {mark}%\n")
        # 可以不要写you get 多少mark


t1 = Mathematics_Related()
t1.reset()
t1.run()
t1.show_mathematics_mark()
