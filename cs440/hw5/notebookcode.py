#!/usr/bin/env python
# coding: utf-8

# $\newcommand{\xv}{\mathbf{x}}
# \newcommand{\Xv}{\mathbf{X}}
# \newcommand{\yv}{\mathbf{y}}
# \newcommand{\zv}{\mathbf{z}}
# \newcommand{\av}{\mathbf{a}}
# \newcommand{\Wv}{\mathbf{W}}
# \newcommand{\wv}{\mathbf{w}}
# \newcommand{\tv}{\mathbf{t}}
# \newcommand{\Tv}{\mathbf{T}}
# \newcommand{\muv}{\boldsymbol{\mu}}
# \newcommand{\sigmav}{\boldsymbol{\sigma}}
# \newcommand{\phiv}{\boldsymbol{\phi}}
# \newcommand{\Phiv}{\boldsymbol{\Phi}}
# \newcommand{\Sigmav}{\boldsymbol{\Sigma}}
# \newcommand{\Lambdav}{\boldsymbol{\Lambda}}
# \newcommand{\half}{\frac{1}{2}}
# \newcommand{\argmax}[1]{\underset{#1}{\operatorname{argmax}}}
# \newcommand{\argmin}[1]{\underset{#1}{\operatorname{argmin}}}$

# # A5:  Min-Conflicts
# 
# * *A5.1*: New version of A5grader.py. Download and extract from [A5grader.tar](https://www.cs.colostate.edu/~anderson/cs440/notebooks/A5grader.tar).  This version includes 5pm as a class meeting time, uses a different random number seed and another few classes in the final test.

# Yibo Xu

# For this assignment, you will use the `min-conflicts` code from the lecture notes to solve the following scheduling problem. <font color="red">Do not change this code in completing this assignment.</font>

# You are in charge of assigning classes to classrooms and times for the
# department. The scheduling is simplified by the fact at this imaginary university each class meets every day. 
# 
# You have been asked to schedule these four class rooms:
# 
#   * CSB 130
#   * CSB 325
#   * CSB 425
#   * Clark 101
#   
# Classes start on the hour. You can only assign classes to the hours of
# 
#   *  8 am
#   *  9 am
#   * 10 am
#   * 11 am
#   * 12 pm
#   *  1 pm
#   *  2 pm
#   *  3 pm
#   *  4 pm
#   *  5 pm
#   
# You must schedule these 37 classes:
# 
#   * CS160, CS163, CS164, CS165, CS192, CS199,
#   * CS220, CS270, CS253, CS245, CS250, CS280,
#   * CS320, CS314, CS356, CS370, CS380, CS390,
#   * CS410, CS414, CS420, CS425, CS430, CS435, CS440, CS445, CS453, 
#   * CS510, CS514, CS520, CS530, CS533, CS535, CS540, CS545, CS548, CS553
# 
# Your schedule must not violate any of the following constraints.
# 
#   * Two classes cannot meet in the same room at the same time.
#   * Classes with the same first digit cannot meet at the same time, because students might take a subset of these in one semester. There is one exception to this rule. CS163 and CS164 can meet at the same time.
#   
# In addition to these constraints, let's add some preferences, which turns this CSP problem into a COP problem.  Let's prefer schedules with the fewest number of classes scheduled at 8 am and 5 pm. 

# The variables for this COP problem are the classes.  The values you assign to each class will be a tuple containing a room and a time.

# ## Required Functions

# ### `assignments = schedule(classes, times, rooms, max_steps, n_solutions_to_test,)`
# 
# Given:
# * `classes`: list of all class names, like 'CS410'
# * `times`: list of all start times, like '10 am' and ' 1 pm'
# * `rooms`: list of all rooms, like 'CSB 325'
# * `max_steps`: maximum number of assignments to try, passed to `min_conflicts` as the last argument
# * `n_solutions_to_test`: call `min_conflicts` this many times.  For each solution, count the number of classes scheduled at 8 am or 5 pm.  Keep track of the lowest number of classes at 8 am and 5 pm and the corresponding assignments of values to variables.
# 
# Return:
# * `assignments`: dictionary of best values assigned to variables (ones that have lowest number of classes scheduled at 8 am or 5pm), like `{'CS410': ('CSB 425', '10 am'), ...}`
# 
# `assignments` will each be `None` if a solution was not found.
# 
# ### `result = constraints_ok(class_name_1, value_1, class_name_2, value_2)`
# 
# Given:
# * `class_name_1`: as above, like 'CS410'
# * `value_1`: tuple containing room and time
# * `class_name_2`: a second class name
# * `value_2`: another tuple containing a room and time
# 
# Returns:
# * `result`: `True` if the assignment of `value_1` to `class_name 1` and `value_2` to `class_name 2` does
# not violate any constraints.  `False` otherwise.
#      
# ### `dataframe = display(assignments, rooms, times)`
# Given
# * `assignments`: returned from your `schedule` function
# * `rooms`: list of all rooms as above
# * `times`: list of all times as above
# Returns:
# * `dataframe`: a `pandas.DataFrame` of the solution, as shown in the example below.

# In[7]:


import random

def min_conflicts(vars, domains, constraints, neighbors, max_steps=1000): 
    """Solve a CSP by stochastic hillclimbing on the number of conflicts."""
    # Generate a complete assignment for all vars (probably with conflicts)
    current = {}
    for var in vars:
        val = min_conflicts_value(var, current, domains, constraints, neighbors)
        current[var] = val
    # Now repeatedly choose a random conflicted variable and change it
    for i in range(max_steps):
        conflicted = conflicted_vars(current, vars, constraints, neighbors)
        if not conflicted:
            return (current, i)
        var = random.choice(conflicted)
        val = min_conflicts_value(var, current, domains, constraints, neighbors)
        current[var] = val
    return (None, None)

def min_conflicts_value(var, current, domains, constraints, neighbors):
    """Return the value that will give var the least number of conflicts.
    If there is a tie, choose at random."""
    return argmin_random_tie(domains[var],
                             lambda val: nconflicts(var, val, current, constraints, neighbors)) 

def conflicted_vars(current, vars, constraints, neighbors):
    "Return a list of variables in current assignment that are in conflict"
    return [var for var in vars
            if nconflicts(var, current[var], current, constraints, neighbors) > 0]

def nconflicts(var, val, assignment, constraints, neighbors):
    "Return the number of conflicts var=val has with other variables."
    # Subclasses may implement this more efficiently
    def conflict(var2):
        val2 = assignment.get(var2, None)
        return val2 != None and not constraints(var, val, var2, val2)
    return len(list(filter(conflict, neighbors[var])))

def argmin_random_tie(seq, fn):
    """Return an element with lowest fn(seq[i]) score; break ties at random.
    Thus, for all s,f: argmin_random_tie(s, f) in argmin_list(s, f)"""
    best_score = fn(seq[0])
    n = 0
    for x in seq:
        x_score = fn(x)
        if x_score < best_score:
            best, best_score = x, x_score; n = 1
        elif x_score == best_score:
            n += 1
            if random.randrange(n) == 0:
                    best = x
    return best


# In[107]:


def schedule(classes, times, rooms, max_steps, n_solutions_to_test):
    domains = {key: [(a,b) for a in rooms for b in times] for key in classes}
    
    neighbors = {var: [v for v in classes if v != var] for var in classes}
    best = {}
    length = 10
    for i in range(n_solutions_to_test):
        solution, step = min_conflicts(classes, domains, constraints_ok, neighbors, max_steps=max_steps)
        count=0
        for clas in classes:
            v = solution.get(clas)
            if v[1] == ' 8 am':
                count = count + 1
            if v[1] == ' 5 pm':
                count = count + 1     
        if count < length:
            length = count
            best = solution
            #print(best)
            print("Solution %s is new best solution found in %s steps, with %s classes at 8 or 5."%(i,step,count))
    return best


# In[108]:


def constraints_ok(class_name_1, value_1, class_name_2, value_2):
    if(class_name_1 == class_name_2):
        return False
    if(value_1[0]==value_2[0] and value_1[1]==value_2[1]):
        return False
    if(class_name_1[2]==class_name_2[2] and value_1[1]==value_2[1]):
        if((class_name_1=='CS163' and  class_name_2=='CS164') or (class_name_2=='CS164' and  class_name_1=='CS163')):
            return True
        else:
            return False    

    return True


# In[109]:


import pandas as pd
def display(assignments, rooms, times):
    dis=pd.DataFrame(columns = rooms, index=[i for i in times],data='')
    for key, value in assignments.items():
        dis.loc[value[1], value[0]]=key
    return dis


# ## Examples

# In[110]:


classes = ['CS160', 'CS163', 'CS164', 'CS165', 'CS192', 'CS199',
           'CS220', 'CS270', 'CS253', 'CS245', 'CS250', 'CS280',
           'CS320', 'CS314', 'CS356', 'CS370', 'CS380', 'CS390',
           'CS410', 'CS414', 'CS420', 'CS425', 'CS430', 'CS435', 'CS440', 'CS445', 'CS453', 
           'CS510', 'CS514', 'CS520', 'CS530', 'CS533', 'CS535', 'CS540', 'CS545', 'CS548', 'CS553']

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


rooms = ['CSB 130', 'CSB 325', 'CSB 425',
         'Clark 101'] #, 'Clark 102']


# In[111]:


len(classes), len(times) * len(rooms)


# In[112]:


random.seed(555)

n_solutions_to_test = 1000
max_steps = 100
assignments = schedule(classes, times, rooms, max_steps,n_solutions_to_test)


# In[113]:


display(assignments, rooms, times)


# ## Check-in

# Do not include this section in your notebook.
# 
# Name your notebook ```Lastname-A5.ipynb```.  So, for me it would be ```Anderson-A5.ipynb```.  Submit the file using the ```Assignment 5``` link on [Canvas](https://colostate.instructure.com/courses/109411).

# ## Grading
# 
# Download [A5grader.tar](http://www.cs.colostate.edu/~anderson/cs440/notebooks/A5grader.tar) and extract `A5grader.py` from it.

# In[114]:


get_ipython().run_line_magic('run', '-i A5grader.py')


# # Extra Credit
# 
# Let's give the freshman a break and try to schedule their courses in the middle of the day.  So, solve the scheduling problem again but with the additional preference of:
# 
#   * prefer schedules with CS1xx courses scheduled at 11 am, 12 pm, or 1pm.
# 
# Create a second version of `schedule` called `schedule_best_for_freshman` that includes this additional preference.  

# In[97]:


def schedule_best_for_freshman(classes, times, classrooms, maxsteps,n_solutions_to_test):
    domains = {key: [(a,b) for a in rooms for b in times] for key in classes}
    cs1xx = {'CS160', 'CS163', 'CS164', 'CS165', 'CS192', 'CS199'}
    neighbors = {var: [v for v in classes if v != var] for var in classes}
    best = {}
    length = 0
    for i in range(n_solutions_to_test):
        solution, step = min_conflicts(classes, domains, constraints_ok, neighbors, max_steps=max_steps)
        count=0
        for clas in classes:
            v = solution.get(clas)
            #print(clas[2])
            if v[1] == '11 am' and clas[2] == '1' :
                count = count + 1
            elif v[1] == '12 pm' and  clas[2]== '1' :
                count = count + 1     
            elif v[1] == ' 1 pm'  and clas[2] == '1':
                count = count + 1  
        #print(count)        
        if count > length:
            length = count
            best = solution
            #print(best)
            print("Solution %s is new best solution found in %s steps, with %s classes at 11, 12 or 1."%(i,step,count))
    return best


# In[98]:


classes = ['CS160', 'CS163', 'CS164', 'CS165', 'CS192', 'CS199',
           'CS220', 'CS270', 'CS253', 'CS245', 'CS250', 'CS280',
           'CS320', 'CS314', 'CS356', 'CS370', 'CS380', 'CS390',
           'CS410', 'CS414', 'CS420', 'CS425', 'CS430', 'CS435', 'CS440', 'CS445', 'CS453', 
           'CS510', 'CS514', 'CS520', 'CS530', 'CS533', 'CS535', 'CS540', 'CS545', 'CS548', 'CS553']

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


rooms = ['CSB 130', 'CSB 325', 'CSB 425',
         'Clark 101'] #, 'Clark 102']

random.seed(555)

n_solutions_to_test = 100
max_steps = 100

a = schedule_best_for_freshman(classes, times, rooms, max_steps,n_solutions_to_test)


# In[89]:


display(a, rooms, times)


# I tried to call the sechedule function firstly, but that always return error like too many unpacked info. So I reweite my sechedule function to find the best solution like cs1xx class in 11,12 and 1 those 3 times.
