import copy
import sys 
  
sys.setrecursionlimit(10**6) 


#States    
def go_to_floor1(state):
    if state[-1]<8 and state[1]>0:
        if state[1]>8-state[-1]:
            new_state = [1] + [state[1] + state[-1] - 8] + [state[2]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [1] + [0] + [state[2]] + [state[3]] + [state[4]] + [state[1] + state[-1]]
        return new_state
    elif state[-1] <= 8 and state[1] ==0:
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
        return new_state
     
        
def go_to_floor2(state):
    if state[-1]<8 and state[2]>0:
        if state[2]>8-state[-1]:
            new_state = [2] + [state[2] + state[-1] - 8] + [state[1]] + [state[3]] + [state[4]] + [8]
        else:
            new_state = [2] + [0] + [state[1]] + [state[3]] + [state[4]] + [state[2] + state[-1]]
        return new_state
    elif state[-1] <= 8 and state[2] ==0:
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
        return new_state
    
def go_to_floor3(state):
    if state[-1]<8 and state[3]>0:
        if state[3]>8-state[-1]:
            new_state = [3] + [state[3] + state[-1] - 8] + [state[2]] + [state[1]] + [state[4]] + [8]
        else:
            new_state = [3] + [0] + [state[2]] + [state[1]] + [state[4]] + [state[3] + state[-1]]
        return new_state
    elif state[-1] <= 8 and state[3] ==0:
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
        return new_state

def go_to_floor4(state):
    if state[-1]<8 and state[4]>0:
        if state[4]>8-state[-1]:
            new_state = [4] + [state[4] + state[-1] - 8] + [state[2]] + [state[1]] + [state[4]] + [8]
        else:
            new_state = [4] + [0] + [state[2]] + [state[1]] + [state[3]] + [state[4] + state[-1]]
        return new_state
    elif state[-1] <= 8 and state[4] ==0:
        new_state = [5] + [state[1]] + [state[2]] + [state[3]] + [state[4]] + [0]
        return new_state



def find_children(state):
    
    children=[]
    
  
    
    floor1_state=copy.deepcopy(state)
    floor1_child=go_to_floor1(floor1_state)
    floor2_state=copy.deepcopy(state)
    floor2_child=go_to_floor2(floor2_state)
    floor3_state=copy.deepcopy(state)
    floor3_child=go_to_floor3(floor3_state)    
    floor4_state=copy.deepcopy(state)
    floor4_child=go_to_floor4(floor4_state)    


    if floor1_child!=None: 
        children.append(floor1_child)

    if floor2_child!=None: 
        children.append(floor2_child)
      
    if floor3_child!=None: 
        children.append(floor3_child)
     
    if floor4_child!=None: 
        children.append(floor4_child)     


    return children



# FRONT Management
def make_front(state):
    return [state]

def expand_front(front, method):
    if method == 'DFS':
        if front:
            print("Front (DFS):")
            print(front)
            node = front.pop(0)
            for child in find_children(node):
                front.insert(0, child)
    
    elif method == 'BFS':
        if front:
            print("Front (BFS):")
            print(front)
            node = front.pop(0)
            for child in find_children(node):
                front.append(child)

    elif method == 'BestFS':
        if front:
            print("Front (BestFS):")
            print(front)
            front.sort(key=lambda x: heuristic_function(x))  # Sort by heuristic value
            node = front.pop(0)
            for child in find_children(node):
                front.append(child)

    else:
        print("Invalid method. Other methods to be added.")
    
    return front

#Heuristic function
def heuristic_function(node):
    return sum(node)

# Basic recursive function to create a search tree
def find_solution(front, closed, goal, method):
    if not front:
        print('_NO_SOLUTION_FOUND_')
    
    elif front[0] in closed:
        new_front = copy.deepcopy(front)
        new_front.pop(0)
        find_solution(new_front, closed, goal, method)
    
    elif front[0] == goal:
        print('_GOAL_FOUND_')
        print(front[0])
    
    else:
        closed.append(front[0])
        front_copy = copy.deepcopy(front)
        front_children = expand_front(front_copy, method)
        closed_copy = copy.deepcopy(closed)
        find_solution(front_children, closed_copy, goal, method)

# Executing the code
def main():
    initial_state = [0, 9, 4, 12, 7, 0]
    goal = [5, 0, 0, 0, 0, 0]


    method = 'DFS'

    print('____BEGIN__SEARCHING____')
    find_solution(make_front(initial_state), [], goal, method)
    

if __name__ == "__main__":
    main()