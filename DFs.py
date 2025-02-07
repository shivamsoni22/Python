from collections import defaultdict

def has_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            if has_cycle(graph, neighbor, visited, rec_stack):
                return True
        elif neighbor in rec_stack:
            return True
    rec_stack.remove(node)
    return False

def detect_cycle(edges, n):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    visited, rec_stack = set(), set()
    for node in range(n):
        if node not in visited:
            if has_cycle(graph, node, visited, rec_stack):
                return True
    return False

print(detect_cycle([(0,1), (1,2), (2,0)], 3))  # Output: True
