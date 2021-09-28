from pprint import pprint

import networkx as nx
import matplotlib.pyplot as plt


def calculate_dijkstra(graph, start):
    distances = [float("inf") for _ in range(len(graph))]
    roots = [None for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]

    distances[start] = 0
    roots[start] = start

    while True:
        shortest_distance = float("inf")
        working_node = -1
        for neighbour_node in range(len(graph)):
            if distances[neighbour_node] < shortest_distance and not visited[neighbour_node]:
                shortest_distance = distances[neighbour_node]
                working_node = neighbour_node

        if working_node == -1:
            return distances, roots

        for neighbour_node in range(len(graph[working_node])):
            if graph[working_node][neighbour_node] != 0 and \
                    distances[neighbour_node] > distances[working_node] + graph[working_node][neighbour_node]:
                distances[neighbour_node] = distances[working_node] + graph[working_node][neighbour_node]
                roots[neighbour_node] = working_node

        visited[working_node] = True


def show_graph(adjacent_array: [[int]]):
    graph = nx.DiGraph()

    for i in range(len(adjacent_array)):
        graph.add_node(get_label_from_index(i))
        for j in range(len(adjacent_array[i])):
            if adjacent_array[i][j] != 0:
                graph.add_edge(get_label_from_index(i), get_label_from_index(j), weight=adjacent_array[i][j])

    nx.draw(graph, with_labels=True)

    # pos = nx.spring_layout(G)
    # edge_labels = nx.get_edge_attributes(G, 'weight')
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.show()


def get_label_from_index(index: int, ascii_offset=65):
    return chr(ascii_offset + index)


def get_index_from_label(label: chr, ascii_offset=65):
    return ord(label) - ascii_offset


def path_to(roots, source, destination):
    if destination is None:
        return "No Destination"
    result: [int] = []
    while True:
        result.append(destination)
        if source == destination:
            break
        destination = roots[destination]
    result.reverse()
    return result


def print_result(distances, roots):
    source = None
    for i in range(len(distances)):
        if distances[i] == 0:
            source = distances[i]
            break
    for i in range(len(distances)):
        path = path_to(roots, source, i)
        labeled_path: [str] = []
        for j in range(len(path)):
            labeled_path.append(get_label_from_index(path[j]))
        print("Node: {0} | Length= {1} | Root= {2} | Path: {3}".format(get_label_from_index(i), str(distances[i]),
                                                                       get_label_from_index(roots[i]), labeled_path))


if __name__ == '__main__':
    #            A, B, C, D, E, F, G, H, I
    adjacent = [[0, 3, 0, 9, 2, 0, 0, 0, 0],  # A
                [3, 0, 2, 5, 6, 5, 0, 0, 0],  # B
                [0, 2, 0, 0, 3, 2, 0, 0, 0],  # C
                [9, 5, 0, 0, 8, 0, 1, 3, 0],  # D
                [2, 6, 3, 8, 0, 3, 7, 6, 2],  # E
                [0, 5, 2, 0, 3, 0, 0, 2, 3],  # F
                [0, 0, 0, 1, 7, 0, 0, 2, 0],  # G
                [0, 0, 0, 0, 6, 2, 4, 0, 6],  # H
                [0, 0, 0, 0, 2, 3, 0, 6, 0]]  # I
    start = "A"

    distances, roots = calculate_dijkstra(adjacent, get_index_from_label(start))
    print_result(distances, roots)

    # show_graph(adjacent)
