from Knowledge_Base import Common_question, Math_related, Engineering_related, Technology_related, Science_related
from experta import watchers
engine2, engine3 = None, None

def choose_2_branches(stem_collection):
    # select 2 branch with higher weightage
    print(stem_collection)
    ls_stem = ['Science', 'Technology', 'Engineering', 'Mathematics']

    br1 = max(stem_collection)
    index_br1 = stem_collection.index(br1)
    branch1 = ls_stem[index_br1]
    stem_collection.remove(br1)
    ls_stem.remove(str(branch1))

    br2 = max(stem_collection)
    index_br2 = stem_collection.index(br2)
    branch2 = ls_stem[index_br2]
    stem_collection.remove(br2)
    ls_stem.remove(str(branch2))

    # in case 3rd element are the same value as
    return branch1, branch2
    # redirect_to_branch(branch1, branch2)


def redirect_to_branch(branch_1, branch_2):
    global engine2, engine3
    if branch_1 == 'Science':
        # redirect to class Science_related
        # ls[0] = Science_related.Science_Related()
        engine2 = Science_related.Science_Related()
    elif branch_1 == 'Technology':
        # redirect to class Technology_related
        # ls[0] = Technology_related.Technology_Related()
        engine2 = Technology_related.Technology_Related()
    elif branch_1 == 'Engineering':
        # redirect to class Engineering_related
        # ls[0] = Engineering_related.Engineering_Related()
        engine2 = Engineering_related.Engineering_Related()
    else:
        # redirect to class Mathematics_related
        # ls[0] = Math_related.Mathematics_Related
        engine2 = Math_related.Mathematics_Related()

    if branch_2 == 'Science':
        # redirect to class Science_related
        engine3 = Science_related.Science_Related()
    elif branch_2 == 'Technology':
        # redirect to class Technology_related
        engine3 = Technology_related.Technology_Related()
    elif branch_2 == 'Engineering':
        # redirect to class Engineering_related
        engine3 = Engineering_related.Engineering_Related()
    else:
        # redirect to class Mathematics_related
        engine3 = Math_related.Mathematics_Related()


# ----------run---------
print("Hello! Here is a simple STEM Expert System to test which "
      "\nfield in STEM you would be interested.")
print("\n-----------------------?WHAT's STEM?-----------------------"
      "\n-----------------------------------------------------------"
      "\nScience, Technology, Engineering and Mathematics (STEM), "
      "\nis a term used to group together these academic disciplines. "
      "\nSTEM is typically used when addressing education policy "
      "\nand curriculum choices in schools to improve competitiveness "
      "\nin science and technology development.\n"
      "\n-----------------------------------------------------------")

print("\nIn this test, you will first being asked some common questions "
      "\nto determine which branches among STEM you are more interested."
      "\nAfter that you will be directed to two branches of STEM."
      "\n-----------------------------------------------------------\n")
# fired_ruled = []
# watchers.watch('RULES')

engine1 = Common_question.Common_Criteria()
engine1.reset()
engine1.run()
b1, b2 = choose_2_branches(engine1.collection())
redirect_to_branch(b1, b2)
engine2.reset()
engine2.run()
engine3.reset()
engine3.run()
m2 = engine2.show_mark()
m3 = engine3.show_mark()

if m2 > m3:
    print(f"\nSTEM ES thinks you are more suitable in {engine2.name} field.")
elif m2 < m3:
    print(f"\nSTEM ES thinks you are more suitable in {engine3.name} field.")
else:   # m2 = m3
    print(f"\nSTEM ES thinks you are more suitable in both {engine2.name} and {engine3.name} fields.")
# print("\n-----------Now STEM ES is going to show you the fired ruled-----------")
# watchers.watch('RULES')
