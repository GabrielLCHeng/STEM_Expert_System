from Knowledge_Base import Science_related, Technology_related, Engineering_related, Math_related

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