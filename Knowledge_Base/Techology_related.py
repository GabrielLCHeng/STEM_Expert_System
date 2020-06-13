from experta import *

class Technology_Related(KnowledgeEngine):
    technology_weight = 0
    total_question = 6

    @DefFacts()
    def initial_fact(self):
        print("Now STEM ES directs you to " + "\033[1m" + "Technology related" + "\033[0m"
              + " session. \nPlease answer 'yes' or 'no' based on the questions given.\n")
        yield Fact(action1='Some silly info related to Technology field')
        yield Fact(f6='Must be innovative.')
        yield Fact(f5='Should have the power to learn lifelong.')
        yield Fact(f4='Interested in Nanotechnology.')
        yield Fact(f3='Know and Interested in 5G network.')
        yield Fact(f2='Interested in Process.')
        yield Fact(f1='Interested in Quantum technology.')

    # ---------------------------------------
    @Rule(Fact(f1='Interested in Quantum technology.'),
          NOT(Fact(respond_f1=W())))
    def f1(self):
        resp = input("Are you interested in Quantum technology?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f1='yes'))
            self.technology_weight += 1

    # ---------------------------------------
    @Rule(Fact(f2='Interested in Process.'),
          NOT(Fact(respond_f2=W())))
    def f2(self):
        resp = input("Are you interested in Process?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f2='yes'))
            self.technology_weight += 1

    # ---------------------------------------
    @Rule(Fact(f3='Know and Interested in 5G network.'),
          NOT(Fact(respond_f3=W())))
    def f3(self):
        resp = input("Do you know and you are interested in 5G network?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f3='yes'))
            self.technology_weight += 1

    # ---------------------------------------
    @Rule(Fact(f4='Interested in Nanotechnology.'),
          NOT(Fact(respond_f4=W())))
    def f4(self):
        resp = input("Are you interested in Nanotechnology?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f4='yes'))
            self.technology_weight += 1

    # ---------------------------------------
    @Rule(Fact(f5='Should have the power to learn lifelong.'),
          NOT(Fact(respond_f5=W())))
    def f5(self):
        resp = input("Do you think yourself as a lifelong learner?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f5='yes'))
            self.technology_weight += 1

    # ---------------------------------------
    @Rule(Fact(f6='Must be innovative.'),
          NOT(Fact(respond_f6=W())))
    def f6(self):
        resp = input("Are you an innovative person?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f6='yes'))
            self.technology_weight += 1

    # ---------------------------------------

    def show_engineering_mark(self):
        mark = int((self.technology_weight/self.total_question)*100)
        print(f"You answered {self.total_question} questions in this 'Technology related' session.\n"
              f"You answered 'Yes' for {self.technology_weight} questions.\n"
              f"You get {mark}%\n")
        # 可以不要写you get 多少mark


# t1 = Technology_Related()
# t1.reset()
# t1.run()
# t1.show_engineering_mark()
