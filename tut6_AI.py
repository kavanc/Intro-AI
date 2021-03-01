# This functino check if selected color for a province satisfy the constraint or not
def check_constraints(graph, state_index, color, c, total_states):
    for i in range(total_states):
        if(graph[state_index][i] == 1 and color[i] == c): #Q1: check if graph[state_index][i] has a neighbour(==1) and its color is same
            return False #constraint not satisified returning false
    return True #constraints satisfied returning true

# Recusrsive function
def apply_color(graph, total_color, color, total_states, state_index):
    if state_index == total_states: #end condition for recursive call
        return True
    
    #iterating for all colors
    for c in range(1, total_color + 1):
        if(check_constraints(graph, state_index, color, c, total_states) == True):
            color[state_index] = c
            if(apply_color(graph, total_color,color, total_states, state_index + 1)== True):  #Q2: hint: if(call apply_color() with next state_index(recursive call) and check if it returns true)
                return True
            color[state_index] = 0


# main function to solve the problem
def csp_problem(graph, total_states, total_color):
    color = {0,0,0,0,0,0,0,0,0,0} #Q3: create list with all zeroes of size total_states
    if(apply_color(graph, total_color, color,total_states,  0) == None):
        print("solution doesn't exist")
        return False   #Q4: print that solution does not exist and return False from here.
        
    print("Solution exists and states can be colored with:")
    for c in color:
        print(color )#Q5: print color in one line - apply required formatting
        #instead of numbers you can endode them to print red, green, blue or any other prefered color combination
    return True

##############################################################################################################################
#code execution starts from here
total_states = 10  #total_states of canada

#creating graph which represent neighbour provinces set - check graph image in previous cell
# do not touch this - this has been already created for you
graph = [[0, 1, 0, 0, 1, 0, 0, 0, 0, 0],[1, 0, 0, 1, 0, 0, 0, 0, 0, 1],[0, 0, 0, 1, 0, 0, 1, 0, 0, 1],[0, 1, 1, 0, 0, 0, 1, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 1, 1, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],[0, 1, 1, 0, 0, 0, 1, 0, 0, 0]]

# feel free to change total_color and check if we can color all provinces of canada with
# selected colors by satisfying neighbouring constrains
total_color = 3

csp_problem(graph, total_states, total_color) # calling function from here

# Expected answer: 1 2 1 3 2 1 2 1 2 3 (not necessary to be the same)