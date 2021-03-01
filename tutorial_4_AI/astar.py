class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0
        
    def __eq__(self, other):
        return self.position == other.position

class Astar:

    def __init__(self, start = None, end = None, graph = None):
        self.start = start
        self.end = end
        self.graph = graph

  
    #Tas: Implement astar search which returns the path cordinates to reach at the end node from star position.
    # you are free to create another inner/outer class or methods in same or seperate cells
    def astart_search(self):
        start_node = Node(None, self.start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node(None, self.end)
        end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while (len(open_list)> 0):

            #Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index
        
            open_list.pop(current_index)
            closed_list.append(current_node)
            self.graph[current_node.position[0]][current_node.position[1]] = 1
            #Found the goal
            if current_node == end_node:
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                return path[::-1]
       
        #Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
             # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(self.graph) - 1) or node_position[0] < 0 or node_position[1] > (len(self.graph[len(self.graph)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if self.graph[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

         # Loop through children
        for child in children:

            # Child is on the closed list
                if len([x for x in closed_list]):
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

#Execution starts form here
if __name__ == '__main__':
    
    #puzzles in form of multidimensional list
    puzzle_1 = [[0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0]]
    puzzle_2 = [[0, 1, 0, 0, 0, 0],
             [1, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 1],
             [0, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 0, 0],
             [0, 0, 1, 0, 0, 0]
             ]
    #start and end node
    start1 = (0, 0)
    end1 = (5, 5)
    start2 = (1,1)
    end2 = (4, 5)
    astar1 = Astar(start1,end1,puzzle_1)
    astar2 = Astar(start2,end2,puzzle_2)
    print("Graph1 path = ", astar1.astart_search()) #Expected output: [(0, 0), (1, 1), (2, 2), (3, 3), (4, 3), (5, 4), (5, 5)]
    print("Graph2 path = ", astar2.astart_search()) #Expected outputz: [(1,1), (2,2), (3,3), (4,4), (4,5)]