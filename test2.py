# 크기가 n인 도넛모양 그래프는 n개의 정점과 n개의 간선이 있음
# 도넛 모양 그래프의 아무 한 점에서 출발해 이용한적 없는 간선을 계속 따라가면 나머지 n-1 개의 정점들을 한 번씩 방문한 뒤 원래 출발했던 정점으로 돌아오게됨

# 크기가 n인 막대 모양 그래프는 n개의 정점과 n-1개의 간선이 있음
# 막대모영 그래프는 임의의 한 정점에서 풀발해 간선을 계속 따라가면 나머지 n-1개의 정점을 한번씩 방문하게 되는 정점이 단 하나 존재함

# 크기가 n인 8자 모양 그래프는 2n+1 개의 정점과 2n+2개의 간선이있음
# 8자 모양 그래프는 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태의 그래프임

edges = [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3],[11, 9], [3, 8]]
result = [4, 0, 1, 2]
from collections import defaultdict


def search_new_edge(edge_dict):
    max_value = 0
    new_edge = 0
    for key, value in edge_dict.items():
        if len(value) > max_value:
            max_value = len(value)
            new_edge = key
    return new_edge


def count_donut(edge_dict, new_edge):
    count = 0
    stack = []
    stack.append(new_edge)
    visit = [0 for _ in range(100 + 1)]
    while stack:
        cur = stack.pop()
        if visit[new_edge] == 2:
            visit[new_edge] = 1
            count += 1
        for next_edge in edge_dict[cur]:
            if visit[next_edge] < 1:
                stack.append(next_edge)
                visit[next_edge] += 1
    return count


def count_linear(edge_dict, new_edge):
    count = 0
    for item in edge_dict[new_edge]:
        stack = []
        valid = True
        visit = defaultdict(int)
        if len(edge_dict[item]) > 1:
            continue
        stack.append(item)
        while stack:
            cur = stack.pop()
            if visit[cur] > 1:
                valid = False
                break
            for item in edge_dict[cur]:
                stack.append(item)
                visit[item] += 1
        if valid:
            count += 1
    return count


def count_eight(edge_dict , new_edge):


def solution(edges):
    answer = []
    edge_dict = defaultdict(list)
    for edge in edges:
        a, b = edge
        edge_dict[a].append(b)
    new_edge = search_new_edge(edge_dict)

    answer.append(new_edge)
    answer.append(count_donut(edge_dict, new_edge))
    answer.append(count_linear(edge_dict,new_edge))
    return answer


sol = solution(edges)
print(sol)
