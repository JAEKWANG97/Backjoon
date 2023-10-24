# DFS 와 BFS 로 출력하라

'''
4 5 1
1 2
1 3
1 4
2 4
3 4
'''
from collections import defaultdict
import copy

vertex , edge_num  , start_node = map(int, input().split())
edges = []

for i in range(edge_num):
    x,y = map(int,input().split())
    edges.append([x,y])

def makeGraph(edges : []):
    edge_dict = defaultdict(list)
    for i , j in edges:
        edge_dict[i].append(j)
        edge_dict[j].append(i)

    for key, value in edge_dict.items():
        edge_dict[key] = sorted(value)
    return edge_dict


# 정점의 index가 작은 것 부터 방문 ^^
def dfs(edge_dict, start_node):
    stack = []
    seen = []
    seen.append(start_node)
    for i in range(len(edge_dict[start_node])):
        stack.append(edge_dict[start_node].pop())
    while stack:
        neighborhood = stack.pop()
        if neighborhood not in seen:
            seen.append(neighborhood)
            if len(seen) == vertex: break
            for x in sorted(edge_dict[neighborhood] , reverse=True):
                if x not in seen:
                    stack.append(x)
    return  seen

def bfs(edge_dict, start_node):
    queue = []
    seen = []
    seen.append(start_node)
    for i in range(len(edge_dict[start_node])):
        queue.append(edge_dict[start_node][i])
    while queue:
        neighborhood = queue.pop(0)
        if neighborhood not in seen:
            seen.append(neighborhood)
            if len(seen) == vertex: break
            for x in sorted(edge_dict[neighborhood]):
                if x not in seen:
                    queue.append(x)
    return  seen
edges_copy = copy.deepcopy(edges)
edge_dict = makeGraph(edges_copy)

arr = dfs(makeGraph(edges) , start_node)
print(*arr)
arr = bfs(makeGraph(edges) , start_node)
print(*arr)