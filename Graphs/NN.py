from collections import deque
from graphs import graph
#TODO TO JEST CHYBA NN ALBO DIJIKSTRA ZROBILEM GO PRZEZ PRZYPADEK
class NN(graph):
    def __init__(self, numNodes,starting_point='a') -> None:
        super().__init__(numNodes)
        self.final_route = None
        # self.current_best_route = None
        # self.current_node = None
        self.checked_nodes = None
        self.starting_point = starting_point
        self.current_node = starting_point
        self.current_best_route = [starting_point]
        for key, value in self.all.items():
            for some_node in value:
                if some_node == self.current_node:
                    value.remove(some_node)

    def check_current_level(self):
        print(f"current level: {self.current_node}")
        current_node = self.get_node(self.current_node)
        #returns list of letters of nodes
        aval_nodes = self.all[self.current_node]

        all_distance = {aval_node: current_node.calculate_distance_to(self.get_node(aval_node)) for aval_node in aval_nodes}
        min_node = min(all_distance, key=all_distance.get)
        self.checked_nodes = [self.current_node]

        del self.all[self.current_node]
        self.current_node = min_node
        self.current_best_route.append(min_node)
        for key, value in self.all.items():
            for some_node in value:
                if some_node == self.current_node:
                    value.remove(some_node)

        return min_node, all_distance[min_node]
