from graphs import graph, graph_path
from queue import Queue

routes = []
routes_weights = []

def BFS(g, current_node):
    print(g)
    layer = g.all[current_node]
    checking_now = Queue()
    for node in g.current[current_node]:
        checking_now.put(node)
    g.reset_graph()


    while not checking_now.empty():
        
        node = checking_now.get()
        for index, route in enumerate(routes):
            if route[-1] == current_node and (route + node) not in routes:
                routes.append(route+node)
                routes_weights.append(routes_weights[index]+g.get_node(current_node).calculate_distance_to(g.get_node(node)))
        
        checking_now.task_done()

    g.remove_node(current_node)
    
        
    

g = graph(4)
print(g)
print('all', g.all)
print('current', g.current)
starting_node = 'a'
first_layer = g.all[starting_node]

for letter in first_layer:
    routes.append(starting_node)
    routes_weights.append(0)

print('----------------------------')
BFS(g, 'a')
BFS(g, 'b')
BFS(g, 'c')
BFS(g, 'd')
print(routes)

# print(routes_weights)
