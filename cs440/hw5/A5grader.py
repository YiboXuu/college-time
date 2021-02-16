run_my_solution = False
assignmentNumber = '5'

import os
import copy
import signal
import numpy as np

if run_my_solution:
    from A5mysolution import *
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

for func in ['schedule', 'constraints_ok', 'display']:
    if func not in dir() or not callable(globals()[func]):
        print('CRITICAL ERROR: Function named \'{}\' is not defined'.format(func))
        print('  Check the spelling and capitalization of the function name.')


print('''
Testing

  constraints_ok(\'CS410\', (\'CSB 130\', \' 9 am\'), \'CS510\', (\'CSB 130\', \' 9 am\'))
''')

try:
    pts = 10
    result = constraints_ok('CS410', ('CSB 130', ' 9 am'), 'CS510', ('CSB 130', ' 9 am'))
    if not result:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Your constraints_ok function correctly returned False')
    else:
        print(f'\n---  0/{pts} points. Your constraints_ok function incorrectly returned True but it should return False.')
except Exception as ex:
    print('\n--- constraints_ok raised the exception\n {}'.format(ex))


print('''
Testing

   constraints_ok(\'CS410\', (\'CSB 130\', \' 9 am\'), \'CS510\', (\'CSB 130\', \'10 am\'))
''')

try:
    pts = 10
    result = constraints_ok('CS410', ('CSB 130', ' 9 am'), 'CS510', ('CSB 130', '10 am'))
    if result:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Your constraints_ok function correctly returned True')
    else:
        print(f'\n---  0/{pts} points. Your constraints_ok function incorrectly returned False but it should be True.')
except Exception as ex:
    print('\n--- constraints_ok raised the exception\n {}'.format(ex))

print('''
Testing

  constraints_ok('CS410', ('CSB 130', '10 am'), 'CS430', ('CSB 425', '10 am'))
''')

try:
    pts = 10
    result = constraints_ok('CS410', ('CSB 130', '10 am'), 'CS430', ('CSB 425', '10 am'))
    if not result:
        exec_grade += 10
        print(f'\n--- {pts}/{pts} points. Your constraints_ok function correctly returned False')
    else:
        print(f'\n---  0/{pts} points. Your constraints_ok function incorrectly returned True but it should return False.')
except Exception as ex:
    print('\n--- constraints_ok raised the exception\n {}'.format(ex))


print('''
Testing

      classes = ['CS160', 'CS163', 'CS164',
              'CS220', 'CS270', 'CS253',
              'CS320', 'CS314', 'CS356', 'CS370',
              'CS410', 'CS414', 'CS420', 'CS430', 'CS440', 'CS445', 'CS453', 'CS464',
              'CS510', 'CS514', 'CS535', 'CS540', 'CS545']

      times = [' 8 am',
               ' 9 am',
               '10 am',
               '11 am',
               '12 pm',
               ' 1 pm',
               ' 2 pm',
               ' 3 pm',
               ' 4 pm',
               ' 5 pm']

      rooms = ['CSB 130', 'CSB 325', 'CSB 425']

      random.seed(111)
      result = schedule(classes, times, rooms, 100, 10)
''')

try:
    pts = 30

    classes = ['CS160', 'CS163', 'CS164',

               'CS220', 'CS270', 'CS253',
               'CS320', 'CS314', 'CS356', 'CS370',
               'CS410', 'CS414', 'CS420', 'CS430', 'CS440', 'CS445', 'CS453', 'CS464',
               'CS510', 'CS514', 'CS535', 'CS540', 'CS545']

    times = [' 8 am',
             ' 9 am',
             '10 am',
             '11 am',
             '12 pm',
             ' 1 pm',
             ' 2 pm',
             ' 3 pm',
             ' 4 pm',
             ' 5 pm']

    rooms = ['CSB 130', 'CSB 325', 'CSB 425']

    random.seed(111)
    result = schedule(classes, times, rooms, 100, 10)

    valid = True
    for a,b in result.items():
        for c,d in result.items():
            if c != a:
                valid = valid and constraints_ok(a, b, c, d)

    if len(result) == 23 and valid:
        exec_grade += pts
        print(f'\n--- {pts}/{pts} points. Your schedule function returned a valid schedule.')
    else:
        print(f'\n---  0/{pts} points. Your schedule function did not return a valid schedule.')
        print(f'     Your returned schedule is')
        print(result)

except Exception as ex:
    print('\n--- schedule raised the exception\n {}'.format(ex))


print('''
Testing a call to schedule again with two more classes

    classes += ['CS554', 'CS551', 'CS552', 'CS555', 'CS898', 'CS899']
    random.seed(333)
    result = schedule(classes, times, rooms, 1000, 10)
    n_classes_at_8 = len([(room, time) for
                          (room, time) in result.values()
                          if time.endswith('8 am')])
    n_classes_at_5 = len([(room, time) for
                          (room, time) in result.values()
                          if time.endswith('5 pm')])
''')

try:
    pts = 30
    classes += ['CS554', 'CS551', 'CS552', 'CS555', 'CS898', 'CS899']
    random.seed(333)
    result = schedule(classes, times, rooms, 1000, 10)
    n_classes_at_8 = len([(room, time) for
                          (room, time) in result.values()
                          if time.endswith('8 am')])
    n_classes_at_5 = len([(room, time) for
                          (room, time) in result.values()
                          if time.endswith('5 pm')])
    if n_classes_at_8 + n_classes_at_5 == 5:
        exec_grade += 30
        print(f'\n--- {pts}/{pts} points. Your schedule function correctly returned solution with 5 classes at 8 am or 5 pm.')
    else:
        print(f'\n---  0/{pts} points. Your schedule function did not return a correct solution.')

except Exception as ex:
    print('\n--- schedule raised the exception\n {}'.format(ex))


name = os.getcwd().split('/')[-1]

print()
print('='*70)
print(f'{name} EXECUTION Grade is {exec_grade} / 90')
print('='*70)


print('''
                
___ / 10 points. Your display function returns the correct pandas.DataFrame.
''')


print()
print('='*70)
print(f'{name} Additional Grade is __ / 10')
print('='*70)

print()
print('='*70)
print(f'{name} FINAL GRADE is  _  / 100')
print('='*70)

print('''
Extra Credit: Earn one point of extra credit for correct result from schedule_best_for_freshman and discussion about it..''')

print(f'\n{name} EXTRA CREDIT is 0 / 1')

if run_my_solution:
    print('##############################################')
    print("RUNNING INSTRUCTOR's SOLUTION!!!!!!!!!!!!")
    print('##############################################')
    pass


