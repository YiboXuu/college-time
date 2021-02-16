run_my_solution = False
assignmentNumber = '6'

import os
import copy
import signal
import numpy as np

if run_my_solution:
    from A6mysolution import *
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
            not isinstance(node, ast.ImportFrom)):
            # not isinstance(node, ast.Global) and
            # not isinstance(node, ast.ClassDef)):
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

for func in ['train_for_regression', 'train_for_classification']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')


print('''
Testing

    X = (np.arange(10) - 5).reshape(-1, 1)
    T = np.sin(X)
    nnet, error_trace = train_for_regression(X, T, [20], 2000, 0.01)
''')

try:
    pts = 30
    X = (np.arange(10) - 5).reshape(-1, 1)
    T = np.sin(X)
    nnet, error_trace = train_for_regression(X, T, [20], 2000, 0.01)
    if error_trace[-1] < 0.1:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Your final value in error_trace is correct (less than 0.1)')
    else:
        print(f'\n---  0/{pts} points. Your final value in error_trace is {error_trace[-1]} but it should be less than 0.1')
except Exception as ex:
    print('\n--- train_for_regression raised the exception\n {}'.format(ex))



print('''
Testing

    X = np.linspace(-10, 10, 100).reshape(2, -1).T
    T = (np.sin(0.1 * np.abs(X[:,0]) * X[:, 1]) > 0.7).astype(int)
    nnet, error_trace = train_for_classification(X, T, [20], 2000, 0.01)
''')

try:
    pts = 30
    X = np.linspace(-10, 10, 100).reshape(2, -1).T
    T = (np.sin(0.1 * np.abs(X[:,0:1]) * X[:, 1:2]) > 0.7).astype(int)
    nnet, error_trace = train_for_classification(X, T, [20], 2000, 0.01)

    if error_trace[-1] > 0.98:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Your final value in error_trace is correct (greater than 0.98)')
    else:
        print(f'\n---  0/{pts} points. Your final value in error_trace is {error_trace[-1]} but it should be greater than 0.98')
except Exception as ex:
    print('\n--- train_for_classification raised the exception\n {}'.format(ex))



name = os.getcwd().split('/')[-1]

print()
print('='*70)
print(f'{name} EXECUTION Grade is {exec_grade} / 60')
print('='*70)


print('''
                
___ / 5 points. DataFrame showing results of train_for_regression.

___ / 15 points. Discussion of train_for_regression results with at least five sentences.

___ / 3 points. DataFrame showing results of train_for_classification.

___ / 2 points. Confusion matrix showing results of best network from train_for_classification.

___ / 15 points. Discussion of train_for_classification DataFrame and confusion matrix 
                 results with at least ten sentences.

''')


print()
print('='*70)
print(f'{name} ADDITIONAL Grade is __ / 40')
print('='*70)

print()
print('='*70)
print(f'{name} FINAL GRADE is  _  / 100')
print('='*70)

print('''

Extra Credit: Earn one point of extra credit for correct application of train_for_regression
              to a second regression data set from the UCI ML Repository and 
              discussion of the result.''')
print('''

Extra Credit: Earn one point of extra credit for correct application of train_for_clsssification
              to a second classification data set from the UCI ML Repository and 
              discussion of the result.''')


print(f'\n{name} EXTRA CREDIT is 0 / 2')

if run_my_solution:
    print('##############################################')
    print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    print('##############################################')
    pass


