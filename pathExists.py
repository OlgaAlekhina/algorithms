from collections import deque


def valid_path(n, edges, source, destination):
    if source == destination:
        return True
    if n == 1:
        return False
        
    vert_dict = {}
    for edge in edges:
        if edge[0] in vert_dict:
            vert_dict[edge[0]].add(edge[1])
        else:
            vert_dict[edge[0]] = {edge[1]}
        if edge[1] in vert_dict:
            vert_dict[edge[1]].add(edge[0])
        else:
            vert_dict[edge[1]] = {edge[0]}
   
    d = deque()
    tested_vert = []
    if destination in vert_dict.get(source):
        return True
    tested_vert.append(source)
    for item in vert_dict.get(source):
        d.append(item)
    
    while d:
        cur_vert = d.popleft()
        if destination in vert_dict.get(cur_vert):
            return True
        tested_vert.append(cur_vert)
        for item in vert_dict.get(cur_vert):
            if item not in tested_vert and item not in d:
                d.append(item)

    return False

print(valid_path(9, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5))

# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
#
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
#
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# Example 2:
#
#
# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.