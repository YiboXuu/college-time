#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Assignment-2:-Iterative-Deepening-Search" data-toc-modified-id="Assignment-2:-Iterative-Deepening-Search-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Assignment 2: Iterative-Deepening Search</a></span><ul class="toc-item"><li><span><a href="#Overview" data-toc-modified-id="Overview-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Overview</a></span></li><li><span><a href="#Required-Code" data-toc-modified-id="Required-Code-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Required Code</a></span></li><li><span><a href="#Grading-and-Check-in" data-toc-modified-id="Grading-and-Check-in-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Grading and Check in</a></span></li><li><span><a href="#Extra-Credit" data-toc-modified-id="Extra-Credit-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Extra Credit</a></span></li></ul></li></ul></div>

# # Assignment 2: Iterative-Deepening Search
# 
# * *A2.1: New A2grader.tar and modified explanation of one of the `depth_limited_search` results.*

# Yibo Xu

# ## Overview

# Implement  the iterative-deepening search algorithm as discussed in our lecture notes and as shown in figures 3.17 and 3.18 in our text book. Apply it to the 8-puzzle and a second puzzle of your choice. 

# ## Code and description

# Iterative deeping depth-first search is a state space search strategy that can found the result by using depth first search repeately with increasing depth limits. According to this, that search have qualities of both depth search and breadth search. That will try to find the goal by searching all the nodes in the tree as the same order as depth-first search. If the answer is not found, that moves to a higher depth-limit in the search tree until reach the maximum search spaces or find the answer. The iterative_deeping_search method are the main function that we can use to iterate over the depth-limit search up until reach the maxiumum search space, which we define in input as lepth-limit.The depth-limited search function that generates the children of a state and calls itself recursively on each of the child states.
# 
# 
# 
# At least four sentences describing the solutions found for the 8 puzzle:
# 
# We can see the graph by using print_state_8p method. Firstly, we find the blank in 8-puzzle by using find_8_blank method. Then we use action_f_8p method to get the action that we can do for the puzzle. For example, we can imagine there is a wall around the 8 puzzles, so every action we do that can not cross the wall, then we follow the order like left, right, up, down. We will finish those actions in take_action_f_8p method, like 'up' then we have to switch the blank with up puzzle.
# 
# At least six sentences describing the second search problem, your implementation of state, and the solutions found:
# 
# That is very similar as the 8 puzzle as I choose to do the 15 puzzle. I used col/4 and row/4 to find the black in 15 puzzle as that is 16 nodes. Also, I just list the 4 nodes 4 times to print it out. For the action_f_15p, I just imagine there is a wall aroung the 16 puzzle, so we can't cross the wall. Such as if 0 is at the leftmost, so we can do left action anymore, that is same as up ,down, right. According to this, I will list the action that we can do in the order of left,right,up,down in this method. In the take_f_action_15p method, we just switch the blank node with the node according to our action. For example, if we want to do up action, then we can switch the blank node with up node by minus 4 because there is 4 col in 1 row. Then we can see the answer by print_path_15p as that will call print_state_15p repeatly until get the right answer, so the answer will follow the Iterative deeping depth-first search method.
# 
# 
# 

# In[1]:


import copy

def find_blank_8p(state):
    row = state.index(0)//3
    col = state.index(0)%3
    return (row,col)

def print_state_8p(start_state):
    zero = start_state.index(0)
    start_state[zero] = "-"
    
    col = 0
    for x in range(3):
            print(start_state[col],start_state[col+1],start_state[col+2])
            col+=3
    start_state[start_state.index("-")] = 0
    
def actions_f_8p(start_state):
    actions = []
    index = find_blank_8p(start_state)

    if index[1] > 0:
        actions.append('left')
    if index[1] < 2:
        actions.append('right')
    if index[0] > 0:
        actions.append('up')
    if index[0] < 2:
        actions.append('down')

    return actions


def take_action_f_8p(state, action):
    if action not in actions_f_8p(state):
        print("erroe action")

    here = state.index(0) #Index of blank
    there = state.index(0) #Index of spot to move blank
    if(action == 'left'):
        there -= 1
    elif(action == 'right'):
        there += 1
    elif(action == 'up'):
        there -= 3
    elif(action == 'down'):
        there += 3

    stateCopy = copy.copy(state)
    stateCopy[here], stateCopy[there] = stateCopy[there], stateCopy[here]
    return stateCopy


# In[2]:


def print_path_8p(start_state, goal_state, path):
    print("Path from")
    print_state_8p(start_state)
    print("to")
    print_state_8p(goal_state)
    print("is "+ str(len(path)) +" nodes long:" )

    space = ''
    for state in path:
        print(' ',space,' ')
        print_state_8p(state)
        print()
        space+=' '
       


# In[11]:


def iterative_deepening_search(start_state, goal_state, actions_f, take_action_f, max_depth):
    for depth in range(max_depth):
        result = depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth)
        if result == 'failure':
            return 'failure'
        if result != 'cutoff':
            result.insert(0,start_state)   
            return result
    return 'cutoff'
    
    

def depth_limited_search(start_state, goal_state, actions_f, take_action_f, depth_limit):
    if start_state == goal_state:
        return []
    elif depth_limit == 0:
        return  'cutoff'
    else:   
        cutoff_occurred = False
        for action in actions_f(start_state):
            child_state = take_action_f(start_state, action)
            result = depth_limited_search(child_state, goal_state, actions_f, take_action_f, depth_limit - 1)
            if result is 'cutoff':
                cutoff_occurred = True
            elif result != 'failure':
                result.insert(0,child_state)
                return result
        if cutoff_occurred:
            return 'cutoff'
        else:
            return 'failure'


# Here are some example results.

# In[12]:


start_state = [1, 0, 3, 4, 2, 5, 6, 7, 8]


# In[13]:


print_state_8p(start_state)


# In[14]:


find_blank_8p(start_state)


# In[15]:


actions_f_8p(start_state)


# In[16]:


take_action_f_8p(start_state, 'down')


# In[17]:


print_state_8p(take_action_f_8p(start_state, 'down'))


# In[18]:


goal_state = take_action_f_8p(start_state, 'down')


# In[19]:


new_state = take_action_f_8p(start_state, 'down')


# In[20]:


new_state == goal_state


# In[21]:


start_state


# In[22]:


path = depth_limited_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 1)
path


# Notice that `depth_limited_search` result is missing the start state.  This is inserted by `iterative_deepening_search`.

# In[23]:


path = depth_limited_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 2)
path


# In[24]:


path = depth_limited_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 3)
path


# Here `depth_limited_search` returns more than the solution path.  This is due to how we implement `depth_limited_search`.  This only happens when we don't find the shortest path.  Of course, when called from `iterative_deepening_search` we do find the shortest path.

# In[25]:


path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 4)
path


# Also notice that the successor states are lists, not tuples.  This is okay, because the search functions for this assignment do not make use of python dictionaries.

# In[26]:


start_state = [4, 7, 2, 1, 6, 5, 0, 3, 8]
path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 3)
path


# In[27]:


start_state = [4, 7, 2, 1, 6, 5, 0, 3, 8]
path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 5)
path


# Humm...maybe we can't reach the goal state from this state.  We need a way to randomly generate a valid start state.

# In[28]:


import random


# In[29]:


random.choice(['left', 'right', 'down', 'up'])


# In[30]:


def random_start_state(goal_state, actions_f, take_action_f, n_steps):
    state = goal_state
    for i in range(n_steps):
        state = take_action_f(state, random.choice(list(actions_f(state))))  # list required because actions_f is generator
    return state


# In[31]:


goal_state = [1, 2, 3, 4, 0, 5, 6, 7, 8]
random_start_state(goal_state, actions_f_8p, take_action_f_8p, 10)


# In[32]:


start_state = random_start_state(goal_state, actions_f_8p, take_action_f_8p, 50)
start_state


# In[33]:


path = iterative_deepening_search(start_state, goal_state, actions_f_8p, take_action_f_8p, 20)
path


# Let's print out the state sequence in a readable form.

# In[34]:


for p in path:
    print_state_8p(p)
    print()


# Here is one way to format the search problem and solution in a readable form.

# In[35]:


print_path_8p(start_state, goal_state, path)


# ## second search
# 

# In[67]:


import copy
def find_blank_15p(state):
    row = state.index(0)//4
    col = state.index(0)% 4
    return (row,col)

def print_state_15p(start_state):
    zero = start_state.index(0)
    start_state[zero] = "-"
    
    col = 0
    for x in range(4):
            print(start_state[col],start_state[col+1],start_state[col+2],start_state[col+3])
            col+=4
    start_state[start_state.index("-")] = 0
    
def actions_f_15p(start_state):
    actions = []
    index = find_blank_15p(start_state)

    if index[1] > 0:
        actions.append('left')
    if index[1] < 3:
        actions.append('right')
    if index[0] > 0:
        actions.append('up')
    if index[0] < 3:
        actions.append('down')

    return actions


def take_action_f_15p(state, action):
    if action not in actions_f_15p(state):
        print("erroe action")

    here = state.index(0) #Index of blank
    there = state.index(0) #Index of spot to move blank
    if(action == 'left'):
        there -= 1
    elif(action == 'right'):
        there += 1
    elif(action == 'up'):
        there -= 4
    elif(action == 'down'):
        there += 4

    stateCopy = copy.copy(state)
    stateCopy[here], stateCopy[there] = stateCopy[there], stateCopy[here]
    return stateCopy



def print_path_15p(start_state, goal_state, path):
    print("Path from")
    print_state_15p(start_state)
    print("to")
    print_state_15p(goal_state)
    print("is "+ str(len(path)) +" nodes long:" )

    space = ''
    for state in path:
        print(' ',space,' ')
        print_state_15p(state)
        print()
        space+=' '


# In[41]:


start_state =[1,2,3,4,5,6,8,0,9,7,10,11,12,14,13,15]


# In[42]:


print_state_15p(start_state)


# In[43]:


find_blank_15p(start_state)


# In[44]:


actions_f_15p(start_state)


# In[45]:


take_action_f_15p(start_state, 'up')


# In[46]:


print_state_15p(take_action_f_15p(start_state, 'down'))


# In[47]:


goal_state = take_action_f_15p(start_state, 'down')
new_state = take_action_f_15p(start_state, 'down')
new_state == goal_state


# In[48]:


start_state


# In[49]:


path = depth_limited_search(start_state, goal_state, actions_f_15p, take_action_f_15p, 1)
path


# In[50]:


path = depth_limited_search(start_state, goal_state, actions_f_15p, take_action_f_15p, 2)
path


# In[51]:


path = depth_limited_search(start_state, goal_state, actions_f_15p, take_action_f_15p, 3)
path


# In[72]:


goalState = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
startState = [1,2,3,4,5,6,7,8,9,10,11,0,13,14,15,12]
path = iterative_deepening_search(startState, goalState, actions_f_15p, take_action_f_15p, 10)
path


# In[74]:


startState = [1,2,3,4,5,6,7,8,0,9,10,11,13,14,15,12]
path = iterative_deepening_search(startState, goalState, actions_f_15p, take_action_f_15p, 10)
path


# In[75]:


print_path_15p(start_state, goal_state, path)


# ## extra credit
#     

# In[26]:


def grid_successors(state):
    row, col = state
    # succs will be list of tuples () rather than list of lists [] because state must
    # be an immutable type to serve as a key in dictionary of expanded nodes
    succs = []
    for r in [-1, 0, 1]:   #check each row
        for c in [-1, 0, 1]:  # check in each col
            newr = row + r
            newc = col + c
            if 0 <= newr <= 9 and 0 <= newc <= 9:  
                succs.append( (newr, newc) )
    return succs

def take_action_f(state,action):
    return action


# In[16]:


grid_successors([1,1])


# In[17]:


path = iterative_deepening_search((0,0), (2,2), grid_successors, take_action_f, 20)
path


# In[18]:


path = iterative_deepening_search((0,0), (1,2), grid_successors, take_action_f, 20)
path


# In[22]:


path = iterative_deepening_search((0,0), (9,9), grid_successors, take_action_f, 20)
path


# In[20]:


path = iterative_deepening_search((0,0), (5,9), grid_successors, take_action_f, 20)
path


# ## Grading and Check in

# Download [A2grader.tar](A2grader.tar) and extract A2grader.py from it, before running next code cell.

# In[54]:


get_ipython().run_line_magic('run', '-i A2grader.py')


# In[ ]:




