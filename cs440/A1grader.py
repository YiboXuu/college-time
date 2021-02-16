run_my_solution = False
assignmentNumber = '1'

import os
import copy
import signal
import os
import numpy as np

if run_my_solution:
    from A1mysolution import *
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

for func in ['search', 'breadth_first_search', 'depth_first_search', 'grid_successors_center_block']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')


succs = {'a': ['b'], 'b':['c', 'd'], 'c':['e'], 'd':['f', 'i'], 'e':['g', 'h', 'i']}
print('\nSearching this graph:\n', succs)
def succsf(s):
    return succs.get(s,[])

print('\nLooking for path from a to b.')
print('  Calling breadth_first_search(''a'', ''b'', successorsf)')
print('       and depth_first_search(''a'', ''b'', successorsf)\n')
bfsCorrect = ['a', 'b']
dfsCorrect = ['a', 'b']
bfs = breadth_first_search('a', 'b', succsf)
dfs = depth_first_search('a', 'b', succsf)

points = 10
if bfs == bfsCorrect:
    exec_grade += points
    print('{}/{} points. Your breadth_first_search found correct solution path of {}'.format(points,points,bfs))
else:
    print(' 0/{} points. Your breadth_first_search did not find correct solution path of {}'.format(points,bfsCorrect))

if dfs == dfsCorrect:
    exec_grade += points
    print('{}/{} points. Your depth_first_search found correct solution path of {}'.format(points,points,dfs))
else:
    print(' 0/{} points. Your depth_first_search did not find correct solution path of {}'.format(points,dfsCorrect))

print('\nLooking for path from a to i.')
print('  Calling breadth_first_search(''a'', ''i'', successorsf)')
print('      and depth_first_search(''a'', ''i'', successorsf)\n')
bfsCorrect = ['a', 'b', 'd', 'i']
dfsCorrect = ['a', 'b', 'c', 'e', 'i']
bfs = breadth_first_search('a', 'i', succsf)
dfs = depth_first_search('a', 'i', succsf)
points = 20
if bfs == bfsCorrect:
    exec_grade += points
    print('{}/{} points. Your breadth_first_search found correct solution path of {}'.format(points, points, bfs))
else:
    print(' 0/{} points. Your breadth_first_search did not find correct solution path of {}'.format(points, bfsCorrect))
if dfs == dfsCorrect:
    exec_grade += points
    print('{}/{} points. Your depth_first_search found correct solution path of {}'.format(points, points, dfs))
else:
    print(' 0/{} points. Your depth_first_search did not find correct solution path of {}'.format(points, dfsCorrect))

print('\nLooking for nonexistent path from a to denver.')
print('  Calling breadth_first_search(''a'', ''denver'', successorsf)')
print('      and depth_first_search(''a'', ''denver'', successorsf)\n')

bfsCorrect = 'Goal not found'
dfsCorrect = 'Goal not found'
bfs = breadth_first_search('a', 'denver', succsf)
dfs = depth_first_search('a', 'denver', succsf)
points = 10
if bfs == bfsCorrect:
    exec_grade += points
    print('{}/{} points. Your breadth_first_search found correct solution path of {}'.format(points, points, bfs))
else:
    print(' 0/{} points. Your breadth_first_search did not find correct solution path of {}'.format(points, bfsCorrect))
if dfs == dfsCorrect:
    exec_grade += points
    print('{}/{} points. Your depth_first_search found correct solution path of {}'.format(points, points, dfs))
else:
    print(' 0/{} points. Your depth_first_search did not find correct solution path of {}'.format(points, dfsCorrect))


name = os.getcwd().split('/')[-1]

print()
print('='*70)
print(f'{name} Execution Grade is {exec_grade} / 80')
print('='*70)

print('''\n__ / 5 points. Correct implementation of the grid_successors_center_block function

__ / 5 points. At least two sentences of text describing changes you made to grid_successors to implement grid_successors_center_block

__ / 5 points. Plots of paths resulting from breadth-first and depth-first searches of the grid

__ / 5 points. At least five sentences of text describing your resulting plots.  How are they different with the center block?''')
             
print()
print('='*70)
print(f'{name} Discussion Grade is __ / 20')
print('='*70)

print()
print('='*70)
print(f'{name} FINAL GRADE is  _  / 100')
print('='*70)

print('''
Extra Credit: Earn one point of extra credit for using your search functions to solve the camel puzzle.''')

print(f'\n{name} EXTRA CREDIT is 0 / 1')

if run_my_solution:
    # print('##############################################')
    # print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    # print('##############################################')
    pass

