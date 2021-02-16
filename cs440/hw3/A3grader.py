run_my_solution = False
assignmentNumber = '3'

import os
import copy
import signal
import numpy as np

if run_my_solution:
    from A3mysolution import *
    # print('##############################################')
    # print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    # print('##############################################')

else:
    
    print('\n======================= Code Execution =======================\n')

    import subprocess, glob, pathlib
    n = assignmentNumber
    nb_names = glob.glob(f'*-A{n}-[0-9].ipynb') + glob.glob(f'*-A{n}.ipynb')
    nb_names = np.unique(nb_names)
    nb_names = sorted(nb_names, key=os.path.getmtime)
    if len(nb_names) > 1:
        print(f'More than one ipynb file found: {nb_names}. Using first one.')
    filename = nb_names[0]
    print('Extracting python code from notebook named \'{}\' and storing in notebookcode.py'.format(filename))
    if not filename:
        raise Exception('Please rename your notebook file to <Your Last Name>-A{}.ipynb'.format(assignmentNumber))
    with open('notebookcode.py', 'w') as outputFile:
        subprocess.call(['jupyter', 'nbconvert', '--to', 'script',
                         filename, '--stdout'], stdout=outputFile)
    # from https://stackoverflow.com/questions/30133278/import-only-functions-from-a-python-file
    import sys
    import ast
    import types
    with open('notebookcode.py') as fp:
        tree = ast.parse(fp.read(), 'eval')
    print('Removing all statements that are not function or class defs or import statements.')
    for node in tree.body[:]:
        if (not isinstance(node, ast.FunctionDef) and
            not isinstance(node, ast.Import) and
            not isinstance(node, ast.ImportFrom) and
            not isinstance(node, ast.ClassDef)):
            # not isinstance(node, ast.ImportFrom)):
            tree.body.remove(node)
    # Now write remaining code to py file and import it
    module = types.ModuleType('notebookcodeStripped')
    code = compile(tree, 'notebookcodeStripped.py', 'exec')
    sys.modules['notebookcodeStripped'] = module
    exec(code, module.__dict__)
    # import notebookcodeStripped as useThisCode
    from notebookcodeStripped import *

exec_grade = 0

for func in ['Astar_search', 'iterative_deepening_search',
             'actions_8p', 'take_action_8p', 'goal_test_8p',
             'run_experiment']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')


print('\nTesting actions_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])')
acts = actions_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])
acts = list(acts)
correct = [('left', 1), ('right', 1), ('up', 1)]
if acts == correct:
    exec_grade += 5
    print('\n--- 5/5 points. Your actions_8p correctly returned', acts)
else:
    print('\n--- 0/5 points. Your actions_8p should have returned', correct, 'but you returned', acts)

print('\nTesting take_action_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], (''up'', 1))')
s = take_action_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], ('up', 1))
correct = ([1, 2, 3, 4, 0, 6, 7, 5, 8], 1)
if s == correct:
    exec_grade += 5
    print('\n--- 5/5 points. Your take actions_8p correctly returned', s)
else:
    print('\n--- 0/5 points. Your take_actions_8p should have returned', correct, 'but you returned', s)

print('\nTesting goal_test_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], [1, 2, 3, 4, 5, 6, 7, 0, 8])')
if goal_test_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], [1, 2, 3, 4, 5, 6, 7, 0, 8]):
    exec_grade += 5
    print('\n--- 5/5 points. Your goal_test_8p correctly True')
else:
    print('\n--- 0/5 points. Your goal_test_8p did not return True')


print('\nTesting Astar_search(1, 2, 3, 4, 5, 6, 7, 0, 8],')
print('                     actions_8p, take_action_8p,')
print('                     lambda s: goal_test_8p(s, [0, 2, 3, 1, 4,  6, 7, 5, 8]),')
print('                     lambda s: h1_8p(s, [0, 2, 3, 1, 4,  6, 7, 5, 8]))')

path = Astar_search([1, 2, 3, 4, 5, 6, 7, 0, 8], actions_8p, take_action_8p,
                   lambda s: goal_test_8p(s, [0, 2, 3, 1, 4,  6, 7, 5, 8]),
                   lambda s: h1_8p(s, [0, 2, 3, 1, 4,  6, 7, 5, 8]))

# print('nNodesExpanded =',nNodesExpanded)
                   

correct = ([[1, 2, 3, 4, 5, 6, 7, 0, 8], [1, 2, 3, 4, 0, 6, 7, 5, 8], [1, 2, 3, 0, 4, 6, 7, 5, 8], [0, 2, 3, 1, 4, 6, 7, 5, 8]], 3)
if path == correct:
    exec_grade += 20
    print('\n--- 20/20 points. Your search correctly returned', path)
else:
    print('\n---  0/20 points. Your search should have returned', correct, 'but you returned', path)



print('\nTesting iterative_deepening_search([1, 2, 3, 4, 5, 6, 7, 0, 8], ')
print('                                 [0, 2, 3, 1, 4,  6, 7, 5, 8],')
print('                                 actions_8p, take_action_8p, 10)')
path = iterative_deepening_search([1, 2, 3, 4, 5, 6, 7, 0, 8],[0, 2, 3, 1, 4,  6, 7, 5, 8], actions_8p, take_action_8p, 10)
if path == correct[0]:
    exec_grade += 15
    print('\n--- 15/15 points. Your search correctly returned', path)
else:
    print('\n---  0/15 points. Your search should have returned', correct[0], 'but you returned', path)


print('\nTesting iterative_deepening_search([5, 2, 8, 0, 1, 4, 3, 7, 6], ')
print('                                 [0, 2, 3, 1, 4,  6, 7, 5, 8],')
print('                                 actions_8p, take_action_8p, 10)')
path = iterative_deepening_search([5, 2, 8, 0, 1, 4, 3, 7, 6],[0, 2, 3, 1, 4,  6, 7, 5, 8], actions_8p, take_action_8p, 10)
if type(path) == str and path.lower() == 'cutoff':
    exec_grade += 15
    print('\n--- 15/15 points. Your search correctly returned', path)
else:
    print('\n---  0/15 points. Your search should have returned ''cutoff'', but you returned', path)



print('\nTesting effective_branching_factor(200, 6, 0.1)')

b = effective_branching_factor(200, 6, 0.1)
correctb = 2.18537
if abs(b - correctb) < 0.3:
    exec_grade += 15
    print('\n--- 15/15 points. Your call to effective_branching_factor correctly returned', b)
else:
    print('\n---  0/15 points. Your call to effective_branching_factor returned', b, 'but it should be search should have returned', correctb)


name = os.getcwd().split('/')[-1]

print()
print('='*70)
print(f'{name} Execution Grade is {exec_grade} / 80')
print('='*70)


print('''
___ / 10 points.  At least 6 meaningful sentences describing your third heuristic function.
                  Describe what it calculates and argue why you think it is admissible.''')

print('''
___ / 10 points.  At least 6 more sentences that discuss the similarities and differences in your
                  results for each search method and heuristic function.''')

print()
print('='*70)
print(f'{name} Additional Grade is __ / 20')
print('='*70)

print()
print('='*70)
print(f'{name} FINAL GRADE is  _  / 100')
print('='*70)

print('''
Extra Credit: Earn one point of extra credit for adding the computation time to your results table
and a discussion of the timing results.''')

print(f'\n{name} EXTRA CREDIT is 0 / 1')

if run_my_solution:
    print('##############################################')
    print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    print('##############################################')
    pass


