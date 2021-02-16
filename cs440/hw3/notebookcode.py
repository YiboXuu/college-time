#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#A3:-A*,-IDS,-and-Effective-Branching-Factor" data-toc-modified-id="A3:-A*,-IDS,-and-Effective-Branching-Factor-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>A3: A*, IDS, and Effective Branching Factor</a></span><ul class="toc-item"><li><span><a href="#Heuristic-Functions" data-toc-modified-id="Heuristic-Functions-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Heuristic Functions</a></span></li><li><span><a href="#Comparison" data-toc-modified-id="Comparison-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Comparison</a></span></li><li><span><a href="#Grading" data-toc-modified-id="Grading-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Grading</a></span></li><li><span><a href="#Extra-Credit" data-toc-modified-id="Extra-Credit-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Extra Credit</a></span></li></ul></li></ul></div>

# Yibo Xu

# # A3: A\*, IDS, and Effective Branching Factor

# For this assignment, implement the Recursive Best-First Search
# implementation of the A\* algorithm given in class.  Name this function `Astar_search`.  Also in this notebook include your `iterative_deepening_search` functions.
# Define a new function named `effective_branching_factor` that returns an estimate of the effective
# branching factor for a search algorithm applied to a search problem.
# 
# So, the required functions are
# 
#    - `Astar_search(start_state, actions_f, take_action_f, goal_test_f, h_f)`
#    - `iterative_deepening_search(start_state, goal_state, actions_f, take_action_f, max_depth)`
#    - `effective_branching_factor(n_nodes, depth, precision=0.01)`, returns the effective branching factor, given the number of nodes expanded and depth reached during a search.
# 
# Apply `iterative_deepening_search` and `Astar_search` to several eight-tile sliding puzzle
# problems. For this you must include your implementations of these functions from Assignment 2. Here we are renaming these functions to not include `_f`, just for simplicity.
# 
#   * `actions_8p(state)`: returns a list of up to four valid actions that can be applied in `state`. With each action include a step cost of 1. For example, if all four actions are possible from this state, return [('left', 1), ('right', 1), ('up', 1), ('down', 1)].
#   * `take_action_8p(state, action)`: return the state that results from applying `action` in `state` and the cost of the one step,
#   
# plus the following function for the eight-tile puzzle:
# 
#   * `goal_test_8p(state, goal)`
#   
# Compare their results by displaying
# solution path depth, number of nodes 
# generated, and the effective branching factor, and discuss the results.  Do this by defining the following function that prints the table as shown in the example below.
# 
#    - `run_experiment(goal_state_1, goal_state_2, goal_state_3, [h1, h2, h3])`
#    
# Define this function so it takes any number of $h$ functions in the list that is the fourth argument.

# In[10]:


import copy
import math


def effective_branching_factor(nodes, depth, precision=0.01):
    if (depth==0):
        return 1

    first = 1
    last = nodes
    found = False
    midpoint = 0


    while first <= last and not found:
        midpoint = (first + last) / 2
        if(midpoint!=1):
            calc=(1-midpoint**(depth+1))/(1-midpoint)
        else:
            calc=1
        if abs(calc - nodes) < precision:
            found = True
        else:
            if nodes < calc:
                last = midpoint
                
            else:
                first = midpoint
                

    return midpoint


# In[11]:


def depth_limited_search(state, goalState, actionsF, takeActionF, depthLimit, cost=0):
    global Nodes
    global Depth
    if(state == goalState):
        return []
    if(depthLimit==0):
        return 'cutoff'
    cutoffOccurred = False
    for action in actionsF(state):
        Nodes+=1
        childState = takeActionF(state, action)
        cost+=childState[1]
        result = depth_limited_search(childState[0], goalState, actionsF, takeActionF, depthLimit-1)
        if(result=='cutoff'):
            cutoffOccurred = True
        elif(result!='failure'):
            result.insert(0, childState[0])
            return result
    if(cutoffOccurred):
        return 'cutoff'
    else:
        return 'failure'



def iterative_deepening_search(startState, goalState, actionsF, takeActionF, maxDepth):
    global Nodes
    global Depth
    for depth in range(maxDepth):
        Depth=depth
        result = depth_limited_search(startState, goalState, actionsF, takeActionF, depth)
        if(result=='failure'):
            return 'failure'
        if(result!='cutoff'):
            result.insert(0, startState)
            return result
        
    return 'cutoff'
      
    


# In[12]:


class Node:

    def __init__(self, state, f=0, g=0, h=0):
        self.state = state
        self.f = f
        self.g = g
        self.h = h

    def __repr__(self):
        return f'Node({self.state}, f={self.f}, g={self.g}, h={self.h})'


    
def Astar_search(start_state, actions_f, take_action_f, goal_test_f, heuristic_f):
    global Nodes
    global prevBest
    prevBest=None
    Nodes=0
    
    h = heuristic_f(start_state)
    start_node = Node(state=start_state, f=0 + h, g=0, h=h)
    return a_star_search_helper(start_node, actions_f, take_action_f, 
                                goal_test_f, heuristic_f, float('inf'))

def a_star_search_helper(parent_node, actions_f, take_action_f, 
                         goal_test_f, heuristic_f, f_max):
    
    global Depth
    global Nodes
    global prevBest

    if goal_test_f(parent_node.state):
        return ([parent_node.state], parent_node.g)
    
    ## Construct list of children nodes with f, g, and h values
    actions = actions_f(parent_node.state)
    if not actions:
        return ('failure', float('inf'))
    
    children = []
    for action in actions:
        Nodes+=1
        (child_state, step_cost) = take_action_f(parent_node.state, action)
        h = heuristic_f(child_state)
        g = parent_node.g + step_cost
        f = max(h + g, parent_node.f)
        child_node = Node(state=child_state, f=f, g=g, h=h)
        children.append(child_node)
        
    while True:
        # find best child
        children.sort(key = lambda n: n.f) # sort by f value
        best_child = children[0]
        if best_child.f > f_max:
            return ('failure', best_child.f)
        # next lowest f value
        alternative_f = children[1].f if len(children) > 1 else float('inf')
        # expand best child, reassign its f value to be returned value
        Depth=min(f_max,alternative_f)
        result, best_child.f = a_star_search_helper(best_child, actions_f,
                                                    take_action_f, goal_test_f,
                                                    heuristic_f,
                                                    min(f_max,alternative_f))
        if result != 'failure':                    #        g
            result.insert(0, parent_node.state)    #       / 
            return (result, best_child.f)  


# ## 8 puzzle functions 

# In[13]:


def find_blank_8p(state):
    row = state.index(0)//3
    col = state.index(0)%3
    return (row,col)

def actions_8p(start_state):
    actions = []
    index = find_blank_8p(start_state)

    if index[1] > 0:
        actions.append(('left',1))
    if index[1] < 2:
        actions.append(('right',1))
    if index[0] > 0:
        actions.append(('up',1))
    if index[0] < 2:
        actions.append(('down',1))

    return actions


# In[14]:


import copy

def take_action_8p(state, action):
    left = ('left',1)
    right= ('right',1)
    up   = ('up',1)
    down = ('down',1)
    here = state.index(0) #Index of blank
    there = state.index(0) #Index of spot to move blank
    if(action == left):
        there -= 1
    elif(action == right):
        there += 1
    elif(action == up):
        there -= 3
    elif(action == down):
        there += 3

    stateCopy = copy.copy(state)
    stateCopy[here], stateCopy[there] = stateCopy[there], stateCopy[here]
    return (stateCopy,1)


def goal_test_8p(state, goal):
    return state == goal


# ## Heuristic Functions
# 
# For `Astar_search` use the following two heuristic functions, plus one more of your own design, for a total of three heuristic functions.
# 
#   * `h1_8p(state, goal)`: $h(state, goal) = 0$, for all states $state$ and all goal states $goal$,
#   * `h2_8p(state, goal)`: $h(state, goal) = m$, where $m$ is the Manhattan distance that the blank is from its goal position,
#   * `h3_8p(state, goal)`: $h(state, goal) = e$, where e is the educlidean distance from blank to its goal position.

# In[15]:


def h1_8p(state, goal):
    return 0

def h2_8p(state,goal):
    startBlank = find_blank_8p(state)        # Get the blank index in the start state
    goalBlank = find_blank_8p(goal)          # Get the blank index in the goal state
    manhattanDistance = abs(startBlank[0]-goalBlank[0])+abs(startBlank[1]-goalBlank[1])
    return manhattanDistance

def h3_8p(state,goal):
    statePosition = find_blank_8p(state)
    goalPosition = find_blank_8p(goal)
    return math.sqrt(abs(statePosition[0]-goalPosition[0])**2+abs(statePosition[1]-goalPosition[1])**2)


# ## Comparison

# Apply all four algorithms (`iterative_deepening_search` plus `Astar_search` with the three heuristic
# functions) to three eight-tile puzzle problems with start state
# 
# $$
# \begin{array}{ccc}
# 1 & 2 & 3\\
# 4 & 0 & 5\\
# 6 & 7 & 8
# \end{array}
# $$
# 
# and these three goal states.
# 
# $$
# \begin{array}{ccccccccccc}
# 1 & 2 & 3  & ~~~~ & 1 & 2 & 3  &  ~~~~ & 1 & 0 &  3\\
# 4 & 0 & 5  & & 4 & 5 & 8  & & 4 & 5 & 8\\
# 6 & 7 & 8 &  & 6 & 0 & 7  & & 2 & 6 & 7
# \end{array}
# $$

# Print a well-formatted table like the following.  Try to match this
# format. If you have time, you might consider learning a bit about the `DataFrame` class in the `pandas` package.  When displayed in jupyter notebooks, `pandas.DataFrame` objects are nicely formatted in html.
# 
#            [1, 2, 3, 4, 0, 5, 6, 7, 8]    [1, 2, 3, 4, 5, 8, 6, 0, 7]    [1, 0, 3, 4, 5, 8, 2, 6, 7] 
#     Algorithm    Depth  Nodes  EBF              Depth  Nodes  EBF              Depth  Nodes  EBF          
#          IDS       0      0  0.000                3     43  3.086               11 225850  2.954         
#         A*h1       0      0  0.000                3    116  4.488               11 643246  3.263         
#         A*h2       0      0  0.000                3     51  3.297               11 100046  2.733         
# 
# Of course you will have one more line for `h3`.

# In[16]:


import pandas as pd
import time


def runExperiment(goalState1, goalState2, goalState3, h):
    """set global variables to find nodes and depth of each search.  for each goal, create a new pandas dataframe and
    execute ebf and time methods to add to dataframe along with nodes and depth.  
    """
    global Depth
    global Nodes
    Depth=0
    Nodes=0
    
    h1_8p = h[0]
    h2_8p = h[1]
    h3_8p = h[2]
    
    for goal in [goalState1,goalState2,goalState3]:
        results=pd.DataFrame(columns=['Algorithm','Depth', 'Nodes', 'EBF','Duration (sec)'])
        print(goal)
        Nodes = 0
        Depth = 0
        start_time = time.time()
        solutionPath = iterative_deepening_search(startState, goal, actions_8p, take_action_8p, 100)
        end_time = time.time()

        results.loc[-1] = ["IDS", Depth,Nodes,effective_branching_factor(Nodes,Depth),end_time-start_time]
        results.index = results.index + 1
        
        start_time = time.time()
        solutionPath =Astar_search(startState, actions_8p, take_action_8p, lambda s: goal_test_8p(s, goal),lambda s: h1_8p(s, goal))
        end_time = time.time()        
        results.loc[-1] = ["A*H1", Depth,Nodes,effective_branching_factor(Nodes,Depth),end_time-start_time]
        results.index = results.index + 1   

        start_time = time.time()
        solutionPath = Astar_search(startState, actions_8p, take_action_8p, lambda s: goal_test_8p(s, goal),lambda s: h2_8p(s, goal))
        end_time = time.time()        
        results.loc[-1] = ["A*H2", Depth,Nodes,effective_branching_factor(Nodes,Depth),end_time-start_time]
        results.index = results.index + 1   
        
        start_time = time.time()
        solutionPath =Astar_search(startState, actions_8p, take_action_8p, lambda s: goal_test_8p(s, goal),lambda s: h3_8p(s, goal))
        end_time = time.time()
        results.loc[-1] = ["A*H3", Depth,Nodes,effective_branching_factor(Nodes,Depth),end_time-start_time]
        results.index = results.index + 1   
        
        print(results.to_string(index=False))
        print()
        print()

    
startState = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goalState1 = [1, 2, 3, 4, 0, 5, 6, 7, 8]
goalState2 = [1, 2, 3, 4, 5, 8, 6, 0, 7]
goalState3 = [1, 0, 3, 4, 5, 8, 2, 6, 7]
runExperiment(goalState1, goalState2, goalState3, [h1_8p, h2_8p, h3_8p])


# ## Description 
# 
# 
# At least 6 meaningful sentences describing your third heuristic function.
#                   Describe what it calculates and argue why you think it is admissible.
# 
# Answer:
# In my third heuristic function that calculate the Euclidean distance, that used math function like d = sqrt((x1-x2)^2+(y1-y2)^2) for caculating distance between 2 spot in 2 dimensions. Euclidean distance is like a crow flies. 
#  That will do a straight line between two spots. As we know a heuristic function is admissible if it never overestimates the distance to the goal vertex, so the function I implement should be admissible because the straight line can never overestimate the distance. Also, we can check the result that we got from running Astar search, we  see that answer is very close to h2 and h1, which prove our heuristic function is admissible.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# ## Description

# At least 6 more sentences that discuss the similarities and differences in your
#    results for each search method and heuristic function.
#                   
# answer:
#  In the second goal, the heuristic that I came up with explores almost 3 times less nodes than the 2nd best (A*H2). For goal number 3, A*H2 explores almost 21 times less nodes than the 2nd best algorithm (Ids). Given the growing difference between ids and the other algorithms with larger depth, it shows that a better heuristic can drastically improve runtimes. Such as A*H2, the nodes reduced many times along with the growing depth. However, that remind me the heuristic should fit the situation, the h3 I implement is not fit well in this situation as nodes suddenly increasing in goal 3.
# 
# In general though, it appears that even a relatively simple heuristic can outperform a standard iterative deepening search as the problem gets larger. For the 2nd goal, A*h2 does slightly greater than IDS. But with goal 3, A*h2 suddenly outperforms IDS by over a factor of 4 times. Even the heuristic that I implemented works better than Ids.
# 
# These results lead me to firmly believe that A* algorithms are absolutely the way to go when it comes to path searching. This is of course assuming the heuristic paired with A* isn't as "dumb" as A*h1 that always returns 0.
#                   
#                   

# 

# 

# First, some example output for the effective_branching_factor function.  During execution, this example shows debugging output which is the low and high values passed into a recursive helper function.

# In[17]:


effective_branching_factor(10, 3)


# 
# The smallest argument values should be a depth of 0, and 1 node.

# In[18]:


effective_branching_factor(1, 0)


# In[19]:


effective_branching_factor(2, 1)


# In[20]:


effective_branching_factor(2, 1, precision=0.000001)


# In[21]:


effective_branching_factor(200000, 5)


# In[22]:


effective_branching_factor(200000, 50)


# Here is a simple example using our usual simple graph search.

# In[23]:


def actions_simple(state):
    succs = {'a': ['b', 'c'], 'b':['a'], 'c':['h'], 'h':['i'], 'i':['j', 'k', 'l'], 'k':['z']}
    return [(s, 1) for s in succs.get(state, [])]

def take_action_simple(state, action):
    return action

def goal_test_simple(state, goal):
    return state == goal

def h_simple(state, goal):
    return 1


# In[24]:


actions = actions_simple('a')
actions


# In[25]:


take_action_simple('a', actions[0])


# In[26]:


goal_test_simple('a', 'a')


# In[27]:


h_simple('a', 'z')


# In[28]:


iterative_deepening_search('a', 'z', actions_simple, take_action_simple, 10)


# In[29]:


Astar_search('a',actions_simple, take_action_simple,
            lambda s: goal_test_simple(s, 'z'),
            lambda s: h_simple(s, 'z'))


# ## Grading

# Download [A3grader.tar](http://www.cs.colostate.edu/~anderson/cs440/notebooks/A3grader.tar) and extract A3grader.py from it.

# In[30]:


get_ipython().run_line_magic('run', '-i A3grader.py')


# ## Extra Credit

# Add a third column for each result (from running `runExperiment`) that is the number of seconds each search required.  You may get the total run time when running a function by doing
# 
#      import time
#     
#      start_time = time.time()
#     
#      < do some python stuff >
#     
#      end_time = time.time()
#      print('This took', end_time - start_time, 'seconds.')
# 
