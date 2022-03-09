# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from tkinter import E
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    stack_of_nodes = util.Stack()
    # (curr_node, action) -> Need to check if visited node before adding action otherwise all wrong
    stack_of_nodes.push((problem.getStartState(), []))
    nodes_visited = []
    actions_taken = []

    while not stack_of_nodes.isEmpty():
        (curr_node, action) = stack_of_nodes.pop()
        
        if problem.isGoalState(curr_node) == True:
            actions_taken = action
            break
        
        if curr_node not in nodes_visited:
            nodes_visited.append(curr_node)
            # Get its successors
            # add successors to top of stack_of_nodes of successors
            successors = problem.getSuccessors(curr_node)
            for i in successors:
                nxt_action = action + [i[1]] # If you use str(y[0]) if adds all the actions together into one word
                # Have to do it like this otrherwise don't use the correct path to get to the goal.
                # Using a list of the actions is just a temporary list of the actions taken but some actions are probably wrong 
                nxt_state = (i[0], nxt_action)
                #print(nxt_state)
                stack_of_nodes.push(nxt_state)
            
    return actions_taken
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue_of_nodes = util.Queue()
    # (curr_node, action) -> Need to check if visited node before adding action otherwise all wrong
    queue_of_nodes.push((problem.getStartState(), []))
    nodes_visited = []
    actions_taken = []

    while not queue_of_nodes.isEmpty():
        (curr_node, action) = queue_of_nodes.pop()
        if problem.isGoalState(curr_node) == True:
            actions_taken = action
            break
        
        if curr_node not in nodes_visited:
            nodes_visited.append(curr_node)
            # Get its successors
            # add successors to top of stack_of_nodes of successors
            successors = problem.getSuccessors(curr_node)
            for i in successors:
                nxt_action = action + [i[1]] # If you use str(y[0]) if adds all the actions together into one word
                # Have to do it like this otrherwise don't use the correct path to get to the goal.
                # Using a list of the actions is just a temporary list of the actions taken but some actions are probably wrong 
                nxt_state = (i[0], nxt_action)
                #print(nxt_state)
                queue_of_nodes.push(nxt_state)
    
    #print('Cost:',problem.getCostOfActions(actions_taken))
    return actions_taken
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    queue_of_nodes = util.PriorityQueue()
    # (curr_node, action) -> Need to check if visited node before adding action otherwise all wrong
    queue_of_nodes.push((problem.getStartState(), [], 0), (0)) # node, action, cost
    nodes_visited = []
    actions_taken = []
    

    while not queue_of_nodes.isEmpty():
        (curr_node, action, cost) = queue_of_nodes.pop()
        if problem.isGoalState(curr_node) == True:
            actions_taken = action
            break
        
        if curr_node not in nodes_visited:
            nodes_visited.append(curr_node)
            # Get its successors
            # add successors to top of stack_of_nodes of successors
            successors = problem.getSuccessors(curr_node)
            for i in successors:
                nxt_action = action + [i[1]] # If you use str(y[0]) if adds all the actions together into one word
                # Have to do it like this otrherwise don't use the correct path to get to the goal.
                nxt_cost = cost + i[2]
                # Using a list of the actions is just a temporary list of the actions taken but some actions are probably wrong 
                nxt_state = (i[0], nxt_action, nxt_cost)
                #print(nxt_state)
                queue_of_nodes.push(nxt_state, nxt_cost)
 

    return actions_taken
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
