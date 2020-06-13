# import engine_main
# from experta import KnowledgeEngine
#
#
# class common_question(engine_main.STEM_career):
#
#     def choose_2_branches(self):
#         # select 2 branch with higher weightage
#         ls_max2 = [self.weight_sci, self.weight_tech, self.weight_eng, self.weight_math]
#         dict_max2 = {self.weight_sci: 'Science', self.weight_tech: 'Technology', self.weight_eng: 'Engineering',
#                      self.weight_math: 'Mathematics'}
#
#         b1 = max(ls_max2)
#         branch1 = dict_max2[b1]
#         ls_max2.remove(b1)
#         b2 = max(ls_max2)
#         branch2 = dict_max2[b2]
#         return branch1, branch2
#
#
#
# # ----------run---------
# engine1 = engine_main.STEM_career()
# engine1.reset()
# engine1.run()
#
# branch_1, branch_2 = common_question.choose_2_branches()
# if branch_1 == 'Science':
#     # redirect to class Science_related
#     pass
# elif branch_1 == 'Technology':
#     # redirect to class Technology_related
#     pass
# elif branch_1 == 'Engineering':
#     # redirect to class Engineering_related
#     pass
# else:   # branch_1 == 'Mathematics'
#     # redirect to class Mathematics_related
#     pass
#
# if branch_2 == 'Science':
#     # redirect to class Science_related
#     pass
# elif branch_2 == 'Technology':
#     # redirect to class Technology_related
#     pass
# elif branch_2 == 'Engineering':
#     # redirect to class Engineering_related
#     pass
# else:   # branch_2 == 'Mathematics'
#     # redirect to class Mathematics_related
#     pass
