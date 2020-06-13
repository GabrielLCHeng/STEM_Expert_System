from Knowledge_Base import Common_question, Science_related, Techology_related, Engineering_related, Math_related


def choose_2_branches(ls):
    # select 2 branch with higher weightage
    dict_max2 = {ls[0]: 'Science', ls[1]: 'Technology',
                 ls[2]: 'Engineering', ls[3]: 'Mathematics'}
    br1 = max(ls)
    branch1 = dict_max2[br1]
    ls.remove(br1)
    br2 = max(ls)
    branch2 = dict_max2[br2]
    # print(branch1, branch2)
    return branch1, branch2


def redirect_to_branch(func):

    branch_1, branch_2 = choose_2_branches(func)
    ls = [None, None]
    if branch_1 == 'Science':
        # redirect to class Science_related
        ls[0] = Science_related.Science_Related()
    elif branch_1 == 'Technology':
        # redirect to class Technology_related
        ls[0] = Techology_related.Technology_Related()
    elif branch_1 == 'Engineering':
        # redirect to class Engineering_related
        ls[0] = Engineering_related.Engineering_Related()
    else:
        # redirect to class Mathematics_related
        ls[0] = Math_related.Mathematics_Related

    if branch_2 == 'Science':
        # redirect to class Science_related
        ls[1] = Science_related.Science_Related
    elif branch_2 == 'Technology':
        # redirect to class Technology_related
        ls[1] = Techology_related.Technology_Related
    elif branch_2 == 'Engineering':
        # redirect to class Engineering_related
        ls[1] = Engineering_related.Engineering_Related
    else:
        # redirect to class Mathematics_related
        ls[1] = Math_related.Mathematics_Related

    return ls[0], ls[1]


# ----------run---------
print("Hello! Here is a simple Expert System to test which field in STEM you would be interested.")
user_name = input("What is your name?\n")
x = 0
if x == 0:
    engine1 = Common_question.Common_Criteria()
    engine1.reset()
    engine1.run()
    x += 1
if x == 1:
    b1, b2 = choose_2_branches(engine1.collection())
    engine1, engine2 = redirect_to_branch(engine1.collection())
# engine2.reset()
# engine3.reset()
# engine2.run()
# engine3.run()
