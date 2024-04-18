import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


class Graph:

    def __init__(self, filename):
        self.vertices = []
        self.edges = []
        self.parse_vertices(filename)

    def parse_vertices(self, filename):
        with open(filename) as f:
            for line in f:
                items = line.strip().split(",")

                vertex = items[0]
                self.vertices.append(vertex)

                adjacent_vertices = items[1:]
                for adjacent in adjacent_vertices:
                    self.edges.append((vertex, adjacent))

    def display(self):
        graph = nx.DiGraph()
        graph.add_edges_from(self.edges)
        graph.add_nodes_from(self.vertices)
        nx.draw(graph, with_labels=True)
        plt.show()


if __name__ == '__main__':
    filename = "test_graph.csv"
    g = Graph(filename)

    g.display()
