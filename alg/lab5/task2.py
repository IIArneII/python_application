def reverse_graph(graph: dict):
    new_graph = {}
    for key, value in graph.items():
        if key not in new_graph:
            new_graph[key] = []
        for v in value:
            if v not in new_graph:
                new_graph[v] = []
            new_graph[v].append(key)
    return new_graph


graph = {"1": ["4"],
         "2": ["1", "3"],
         "3": ["5"],
         "4": [],
         "5": ["1", "2"]}

print(''.join([f'{key}: {value}\n' for key, value in reverse_graph(graph).items()]))
