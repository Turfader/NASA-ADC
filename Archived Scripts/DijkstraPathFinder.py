import math
import csv
import os
import DataProcessor as dp

nodes = []

class Points:
    def __init__(self):
        pass

    def __init__(self, x, y, z):
        self.xPos = float(x)
        self.yPos = float(y)
        self.zPos = float(z)
        self.index = len(nodes)

    def __init__(self, x, y, z, slope):
        self.xPos = float(x)
        self.yPos = float(y)
        self.zPos = float(z)
        self.slope = float(slope)
        self.index = len(nodes)

    def getData(self):
        return (self.xPos, self.yPos, self.zPos, self.index)

def generateStartingPoints():

    processedDataPath = dp.rect_file_path
    processedDataPath = processedDataPath.replace("\\", "/")

    with open(processedDataPath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dataList = list(csv_reader)

        for i in range(1, len(dataList)):
            nodes.append(Points(dataList[i][0], dataList[i][1], dataList[i][2], dataList[i][3]))


def printAllPoints(arr):
    for i in range(len(arr)):
        print(arr[i].getData())

def calculateDistance(point1, point2):

    number = math.sqrt((point1.xPos - point2.xPos)*(point1.xPos - point2.xPos) +
                     (point1.yPos - point2.yPos)*(point1.yPos - point2.yPos) +
                     (point1.zPos - point2.zPos)*(point1.zPos - point2.zPos))

    #print("dist between ", point2.index, " and ", point1.index, " is ",number)

    return number

def calculateValue(point1, point2):
    distMod = 1

    distance = calculateDistance(point1, point2)
    value = distance * distMod
    return value

def calculateNeighbors(node):
    misc_data_path = dp.misc_path
    misc_data_path = misc_data_path.replace("\\", "/")
    with open(misc_data_path, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        full_list = list(csv_reader)

        x_and_y_dims = int(full_list[0][0])
        # dist_btw_pts = float(full_list[1][0])
        # min_height = float(full_list[2])



    maxXPos, maxYPos = x_and_y_dims, x_and_y_dims
    minXPos, minYPos = 0, 0

    if node.slope >= 20:
        return

    if 0<=node.index-1<len(nodes) and nodes[node.index-1].xPos >= minXPos:
        init_graph[node][nodes[node.index-1]] = calculateValue(nodes[node.index-1], node)
        if 0<=node.index-maxXPos-1<len(nodes) and nodes[node.index-maxXPos-1].yPos >= minYPos:
            init_graph[node][nodes[node.index-maxXPos-1]] = calculateValue(nodes[node.index-maxXPos-1], node)
        if 0<=node.index+maxXPos-1<len(nodes) and nodes[node.index+maxXPos-1].yPos <= maxYPos:
            init_graph[node][nodes[node.index+maxXPos-1]] = calculateValue(nodes[node.index+maxXPos-1], node)

    if 0<=node.index - maxXPos<len(nodes) and nodes[node.index - maxXPos].yPos >= minYPos:
        init_graph[node][nodes[node.index - maxXPos]] = calculateValue(nodes[node.index - maxXPos], node)
    if 0<=node.index + maxXPos<len(nodes) and nodes[node.index + maxXPos].yPos <= maxYPos:
        init_graph[node][nodes[node.index + maxXPos]] = calculateValue(nodes[node.index + maxXPos], node)


    if 0<=node.index+1<len(nodes) and nodes[node.index+1].xPos <= maxXPos:
        init_graph[node][nodes[node.index+1]] = calculateValue(nodes[node.index+1], node)
        if 0<=node.index-maxXPos+1<len(nodes) and nodes[node.index-maxXPos+1].yPos >= minYPos:
            init_graph[node][nodes[node.index-maxXPos+1]] = calculateValue(nodes[node.index-maxXPos+1], node)
        if 0<=node.index+maxXPos+1<len(nodes) and nodes[node.index+maxXPos+1].yPos <= maxYPos:
            init_graph[node][nodes[node.index+maxXPos-1]] = calculateValue(nodes[node.index+maxXPos-1], node)

#------------------------------------------------------------------------------------------

import sys

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):

        '''
        This method makes sure that the graph is symmetrical. In other words, if there's a path
        from node A to B with a value V, there needs to be a path from node B to node A with a value V.
        '''

        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) is False:
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

# end graph class


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    # We'll use max_value to initialize the "infinity" value of the unvisited nodes
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
        print(len(unvisited_nodes))

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]

    # Add the start node manually
    path.append(start_node)

    path = path[::-1]
    print("\nWe found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(str(x.index) for x in path))
    for i in range(len(path)):
        print(path[i].getData())


#---------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    generateStartingPoints()
    # printAllPoints(nodes)


    init_graph = {}
    for node in nodes:
        init_graph[node] = {}


    for node in nodes:
        calculateNeighbors(node)

    graph = Graph(nodes, init_graph)

    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=nodes[0])
    print("Djikstra Success")
    print_result(previous_nodes, shortest_path, start_node=nodes[0], target_node=nodes[24]) # change the starting nodes to test. 
                                                                                            #Make sure you dont start on a node with slope > 20

#---------------------------------------------------------------------------------------------------------------
