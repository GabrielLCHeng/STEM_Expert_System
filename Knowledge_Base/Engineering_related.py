from experta import *

class Engineering_Related(KnowledgeEngine):
    engineering_weight = 0
    total_question = 7

    @DefFacts()
    def initial_fact(self):
        print("\nNow STEM ES directs you to " + "\033[1m" + "Engineering related" + "\033[0m"
              + " session. \nPlease answer 'yes' or 'no' based on the questions given.\n")
        yield Fact(action1='Some silly info related to Engineering field')
        yield Fact(f7='Interested in Biomedical Engineering.')
        yield Fact(f6='Interested in Mechanical Engineering.')
        yield Fact(f5='Interested in Electrical Engineering.')
        yield Fact(f4='Interested in Civil Engineering.')
        yield Fact(f3='Interested in Chemical Engineering.')
        yield Fact(f2='Interested in Calculation.')
        yield Fact(f1='Interested in Physics.')

    # ---------------------------------------
    @Rule(Fact(f1='Interested in Physics.'),
          NOT(Fact(respond_f1=W())))
    def f1(self):
        resp = input("Are you interested in Physics?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f1='yes'))
            self.engineering_weight += 1

    # ---------------------------------------
    @Rule(Fact(f2='Interested in Calculation.'),
          NOT(Fact(respond_f2=W())))
    def f2(self):
        resp = input("Are you interested in Calculation?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f2='yes'))
            self.engineering_weight += 1

    # ---------------------------------------
    @Rule(Fact(f3='Interested in Chemical Engineering.'),
          NOT(Fact(respond_f3=W())))
    def f3(self):
        resp = input("Are interested in Chemical Engineering?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f3='yes'))
            self.engineering_weight += 1

    # ---------------------------------------
    @Rule(Fact(f4='Interested in Civil Engineering.'),
          NOT(Fact(respond_f4=W())))
    def f4(self):
        resp = input("Are you interested in Civil Engineering?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f4='yes'))
            self.engineering_weight += 1

    # ---------------------------------------
    @Rule(Fact(f5='Interested in Electrical Engineering.'),
          NOT(Fact(respond_f5=W())))
    def f5(self):
        resp = input("Are you interested in Electrical Engineering?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f5='yes'))
            self.engineering_weight += 1

    # ---------------------------------------
    @Rule(Fact(f6='Interested in Mechanical Engineering.'),
          NOT(Fact(respond_f6=W())))
    def f6(self):
        resp = input("Are you interested in Mechanical Engineering?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f6='yes'))
            self.engineering_weight += 1

    # ---------------------------------------
    @Rule(Fact(f7='Interested in Biomedical Engineering.'),
          NOT(Fact(respond_f7=W())))
    def f7(self):
        resp = input("Are you interested in Biomedical Engineering?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f7='yes'))
            self.engineering_weight += 1
    # ---------------------------------------

    def show_engineering_mark(self):
        mark = int((self.engineering_weight / self.total_question) * 100)
        print(f"You answered {self.total_question} questions in this 'Engineering related' session.\n"
              f"You answered 'Yes' for {self.engineering_weight} questions.\n"
              f"You get {mark}%\n")
        # 可以不要写you get 多少mark


# t1 = Engineering_Related()
# t1.reset()
# t1.run()
# t1.show_engineering_mark()
