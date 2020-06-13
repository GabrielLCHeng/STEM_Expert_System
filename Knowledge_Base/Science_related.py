from experta import *

class Science_Related(KnowledgeEngine):
    science_weight = 0
    total_question = 12

    @DefFacts()
    def initial_fact(self):
        print("Now STEM ES directs you to " + "\033[1m" + "Science related" + "\033[0m"
              + " session. \nPlease answer 'yes' or 'no' based on the questions given.\n")
        yield Fact(action1='Some silly info related to Science field')
        yield Fact(f12='Interested in Philosophy.')
        yield Fact(f11='Interested in Political Science.')
        yield Fact(f10='Interested in Social science.')
        yield Fact(f9='Interested in Education.')
        yield Fact(f8='Interested in Arts.')
        yield Fact(f7='Interested in Astronomy.')
        yield Fact(f6='Interested in Biology.')
        yield Fact(f5='Interested in Chemistry.')
        yield Fact(f4='Interested in Physics.')
        yield Fact(f3='Interested in Statistics.')
        yield Fact(f2='Like solving mathematical problems.')
        yield Fact(f1='Interested in Logic.')

    # ---------------------------------------
    @Rule(Fact(f1='Interested in Logic.'),
          NOT(Fact(respond_f1=W())))
    def f1(self):
        resp = input("Are you interested in logic?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f1='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f2='Like solving mathematical problems.'),
          NOT(Fact(respond_f2=W())))
    def f2(self):
        resp = input("Do you like solving mathematical problems?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f2='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f3='Interested in Statistics.'),
          NOT(Fact(respond_f3=W())))
    def f3(self):
        resp = input("Are you interested in Statistics?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f3='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f4='Interested in Physics.'),
          NOT(Fact(respond_f4=W())))
    def f4(self):
        resp = input("Does Physics interest you?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f4='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f5='Interested in Chemistry.'),
          NOT(Fact(respond_f5=W())))
    def f5(self):
        resp = input("Does Chemistry interest you?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f5='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f6='Interested in Biology.'),
          NOT(Fact(respond_f6=W())))
    def f6(self):
        resp = input("Does Biology interest you?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f6='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f7='Interested in Astronomy.'),
          NOT(Fact(respond_f7=W())))
    def f7(self):
        resp = input("Are you interested in Astronomy?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f7='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f8='Interested in Arts.'),
          NOT(Fact(respond_f8=W())))
    def f8(self):
        resp = input("Are you interested in Arts?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f8='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f9='Interested in Education.'),
          NOT(Fact(respond_f9=W())))
    def f9(self):
        resp = input("Are you interested in Education?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f9='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f10='Interested in Social science.'),
          NOT(Fact(respond_f10=W())))
    def f10(self):
        resp = input("Are you interested in Social science "
                     "relevant field?\n(Cognitive Science, Religious "
                     "Studies, Law, Sociology, etc)\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f10='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f11='Interested in Political Science.'),
          NOT(Fact(respond_f11=W())))
    def f11(self):
        resp = input("Are you interested in Political Science?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f11='yes'))
            self.science_weight += 1

    # ---------------------------------------
    @Rule(Fact(f12='Interested in Philosophy.'),
          NOT(Fact(respond_f12=W())))
    def f12(self):
        resp = input("Are you interested in Philosphy?\n")
        if resp == 'yes' or resp == 'y' or resp == 'Yes' or resp == 'Y':
            self.declare(Fact(respond_f12='yes'))
            self.science_weight += 1

    # ---------------------------------------
    def show_science_mark(self):
        mark = int((self.science_weight/self.total_question)*100)
        print(f"You answered {self.total_question} questions in this 'Science related' session.\n"
              f"You answered 'Yes' for {self.science_weight} questions.\n"
              f"You get {mark}%\n")
        # 可以不要写you get 多少mark


# t1 = Science_Related()
# t1.reset()
# t1.run()
# t1.show_science_mark()
