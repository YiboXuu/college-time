run_my_solution = False
assignmentNumber = '2'

import os
import copy
import signal
import os
import numpy as np

if run_my_solution:
    from A2mysolution import *
    # print('##############################################')
    # print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    # print('##############################################')

else:
    
    print('\n======================= Code Execution =======================\n')

    import subprocess, glob, pathlib
    nb_name = '*A{}.ipynb'
    # nb_name = '*.ipynb'
    filename = next(glob.iglob(nb_name.format(assignmentNumber)), None)
    print('Extracting python code from notebook named \'{}\' and storing in notebookcode.py'.format(filename))
    if not filename:
        raise Exception('Please rename your notebook file to <Your Last Name>-A{}.ipynb'.format(assignmentNumber))
    with open('notebookcode.py', 'w') as outputFile:
        subprocess.call(['jupyter', 'nbconvert', '--to', 'script',
                         nb_name.format(assignmentNumber), '--stdout'], stdout=outputFile)
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

for func in ['iterative_deepening_search', 'depth_limited_search',
             'find_blank_8p', 'actions_f_8p', 'take_action_f_8p', 'print_state_8p', 'print_path_8p']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')


######################################################################

succs = {'a': ['b', 'z', 'd'], 'b':['a'], 'e':['z'], 'd':['y'], 'y':['z']}
print('\nSearching this graph:\n', succs)
print('\nLooking for path from a to y with max depth of 1.')

def aF(state):
    import copy
    return copy.copy(succs.get(state,[]))
def tAF(state, action):
    return action

path = iterative_deepening_search('a', 'y', aF, tAF, 1)
if type(path) == str and path.lower() == 'cutoff':
    exec_grade += 5
    print(' 5/ 5 points. Your search correctly returned', path)
else:
    print(' 0/ 5 points. Your search should have returned ''cutoff''. You returned', path)

print('\nLooking for path from a to z with max depth of 5.')
path = iterative_deepening_search('a', 'z', aF, tAF, 5)
if path == ['a', 'z']:
    exec_grade += 10
    print('10/10 points. Your search correctly returned', path)
else:
    print(' 0/10 points. Your search should have returned', ['a', 'z'])


print('\nTesting find_blank_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])')
r, c = find_blank_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])
if r == 2 and c == 1:
    exec_grade += 5
    print(' 5/ 5 points. Your find_blank_8p correctly returned', r, c)
else:
    print(' 0/ 5 points. Your find_blank_8p should have returned 2 1 but you returned', r, c)

print('\nTesting actions_f_8p([1, 2, 3, 4, 5, 6, 7, 0, 8])')
acts = list(actions_f_8p([1, 2, 3, 4, 5, 6, 7, 0, 8]))
correct = ['left', 'right', 'up']
if sorted(acts) == sorted(correct):
    exec_grade += 10
    print('10/10 points. Your actions_f_8p correctly returned', acts)
else:
    print(' 0/10 points. Your actions_f_8p should have returned', correct, 'but you returned', acts)
    
print('\nTesting take_action_f_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], ''up'')')
s = take_action_f_8p([1, 2, 3, 4, 5, 6, 7, 0, 8], 'up')
correct = [1, 2, 3, 4, 0, 6, 7, 5, 8]
if s == correct:
    exec_grade += 10
    print('10/10 points. Your take_actions_f_8p correctly returned', s)
else:
    print(' 0/10 points. Your take_actions_f_8p should have returned', correct, 'but you returned', s)


print('''
Testing iterative_deepening_search([1, 2, 3, 4, 5, 6, 7, 0, 8],
                                   [0, 2, 3, 1, 4,  6, 7, 5, 8],
                                    actions_f_8p, take_action_f_8p, 5)''')
path = iterative_deepening_search([1, 2, 3, 4, 5, 6, 7, 0, 8],[0, 2, 3, 1, 4,  6, 7, 5, 8], actions_f_8p, take_action_f_8p, 5)
correct = [[1, 2, 3, 4, 5, 6, 7, 0, 8], [1, 2, 3, 4, 0, 6, 7, 5, 8], [1, 2, 3, 0, 4, 6, 7, 5, 8], [0, 2, 3, 1, 4, 6, 7, 5, 8]]
if path == correct:
    exec_grade += 20
    print('20/20 points. Your search correctly returned')
    for s in path:
        print('              ', s)
else:
    print(' 0/20 points. Your search should have returned')
    for s in correct:
        print('              ', s)
    print('              but you returned')
    for s in path:
        print('              ', s)

print('''
Testing iterative_deepening_search([5, 2, 8, 0, 1, 4, 3, 7, 6],
                                   [0, 2, 3, 1, 4,  6, 7, 5, 8],
                                   actions_f_8p, take_action_f_8p, 10)''')
path = iterative_deepening_search([5, 2, 8, 0, 1, 4, 3, 7, 6],[0, 2, 3, 1, 4,  6, 7, 5, 8], actions_f_8p, take_action_f_8p, 10)
if type(path) == str and path.lower() == 'cutoff':
    exec_grade += 10
    print('10/10 points. Your search correctly returned ''cutoff''.')
else:
    print(' 0/10 points. Your search should have returned ''cutoff'', but you returned', path)


name = os.getcwd().split('/')[-1]

print()
print('='*70)
print(f'{name} Execution Grade is {exec_grade} / 70')
print('='*70)


print('''\n__ / 10 points. At least four sentences describing the solutions found for the 8 puzzle.

__ / 20 points. At least six sentences describing the second search problem, your implementation 
               of state, and the solutions found.''')
             
print()
print('='*70)
print(f'{name} Additional Grade is __ / 30')
print('='*70)


print()
print('='*70)
print(f'{name} FINAL GRADE is  _  / 100')
print('='*70)

print('''
Extra Credit: Earn one point of extra credit for using your search functions to solve the variation
              of the grid problem in Assignment 1.''')

print(f'\n{name} EXTRA CREDIT is 0 / 1')

if run_my_solution:
    print('##############################################')
    print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    print('##############################################')
    pass

