run_my_solution = False
assignmentNumber = '4'

import os
import copy
import signal
import numpy as np

if run_my_solution:
    from A4mysolution import *
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
    print(nb_names)
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
            # not isinstance(node, ast.Global) and
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

exec_grade = 0

for func in ['print_state', 'get_valid_moves', 'make_move', 'train_Q', 'test_Q']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')

print('''
Testing

  state = [[1], [2,3], [4, 5]]
  moves = get_valid_moves(state)
''')

try:
    pts = 5
    state = [[1], [2,3], [4, 5]]
    moves = get_valid_moves(state)
    correct = [[1, 2], [1, 3], [2, 3]]
    if sorted(moves) == sorted(correct):
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned {moves}')
    else:
        print(f'\n---  0/{pts} points. Incorrect moves. Should have returned {correct}.')
except Exception as ex:
    print('\n--- get_valid_voves raised the exception\n {}'.format(ex))


print('''
Testing

    state = [[], [], [1, 2, 3, 4, 5]]
    moves = get_valid_moves(state)
''')

try:
    pts = 5
    state = [[], [], [1, 2, 3, 4, 5]]
    moves = get_valid_moves(state)
    correct = [[3, 1], [3, 2]]
    if sorted(moves) == sorted(correct):
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned {moves}')
    else:
        print(f'\n---  0/{pts} points. Incorrect moves. Should have returned {correct}.')
except Exception as ex:
    print('\n--- get_valid_voves raised the exception\n {}'.format(ex))



# def equalNestedLists(a, b):
#     if len(a) != len(b):
#         return False
#     for i, sub in enumerate(a):
#         if sub != b[i]:
#             return False
#     return True


print('''
Testing

    state = [[], [], [1, 2, 3, 4, 5]]
    new_state = make_move(state, [3, 1])
''')

try:
    pts = 5
    state = [[], [], [1, 2, 3, 4, 5]]
    new_state = make_move(state, [3, 1])
    correct = [[1], [], [2, 3, 4, 5]]
    if new_state == correct:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned {new_state}')
    else:
        print(f'\n---  0/{pts} points. Incorrect new_state. Should have returned {correct}.')
except Exception as ex:
    print('\n--- make_move raised the exception\n {}'.format(ex))


print('''
Testing

    state = [[1, 2], [3], [4, 5]]
    new_state = make_move(state, [1, 3])
''')

try:
    pts = 5
    state = [[1, 2], [3], [4, 5]]
    new_state = make_move(state, [1, 3])
    correct = [[2], [3], [1, 4, 5]]
    if new_state == correct:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned {new_state}')
    else:
        print(f'\n---  0/{pts} points. Incorrect new_state. Should have returned {correct}.')
except Exception as ex:
    print('\n--- make_move raised the exception\n {}'.format(ex))



print('''
Testing

    Q, steps = train_Q(1000, 0.5, 0.7, get_valid_moves, make_move)
''')

try:
    pts = 10
    Q, steps = train_Q(1000, 0.5, 0.7, get_valid_moves, make_move)
    if len(steps) == 1000:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned list of steps that has 1000 elements.')
    else:
        print(f'\n---  0/{pts} points. The list steps has {len(steps)} but it should have 1000 elements.')

    pts = 10
    if len(Q) > 700:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned a Q dictionary with at least 700 elements.')
    else:
        print(f'\n---  0/{pts} points. Q should have at least 700 elements, yours has {len(Q)}.')

except Exception as ex:
    print('\n--- train_Q raised the exception\n {}'.format(ex))



print('''
Testing

    path = test_Q(Q, 20, get_valid_moves, make_move)
''')

try:
    pts = 20
    path = test_Q(Q, 500, get_valid_moves, make_move)
    if len(path) < 40:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Correctly returned path with fewer than 40 states.')
    else:
        print(f'\n---  0/{pts} points. Returned path with {len(path)} states, but this should be less than 40.')

except Exception as ex:
    print('\n--- train_Q raised the exception\n {}'.format(ex))

    
name = os.getcwd().split('/')[-1]

print()
print('='*70)
print(f'{name} Execution Grade is {exec_grade} / 60')
print('='*70)


print('''
                
___ / 10 points. Correct plot of the number of steps in the solution path versus the
                 number of repetitions.

___ / 10 points. Add markdown cells in which you describe the Q learning algorithm
                 and your implementation of Q learning as applied to the 
                 Towers of Hanoi problem.

___ / 10 points. Add code cells to examine several Q values from the start state
                 with different moves and discuss if the Q values make sense.

___ / 10 points. Also add code cells to examine several Q values from one or two states
                 that are two steps away from the goal and discuss if these Q values make sense.
''')

print()
print('='*70)
print(f'{name} Additional Grade is __ / 40')
print('='*70)

print()
print('='*70)
print(f'{name} FINAL GRADE is  _  / 100')
print('='*70)

print('''
Extra Credit: Earn one point of extra credit for your code for solving
the Towers of Hanoi puzzle with four pegs and five disks and the experiments
and discussion of results.''')

print(f'\n{name} EXTRA CREDIT is 0 / 1')

if run_my_solution:
    print('##############################################')
    print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    print('##############################################')
    pass


