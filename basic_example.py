import numpy as np
import itertools
import random


class Network:
    def __init__(self, size):
        self.size = size
        self.nodes = []

    def init_normal_nodes(self):
        counter = 0
        biases = np.random.normal(0.5, 0.2, self.size)
        elasticities = np.random.normal(0, 0.4, self.size)
        for bias, elasticity in zip(biases, elasticities):
            node = Node(bias, elasticity, counter)
            self.nodes.append(node)
            counter += 1

    def add_connection(self, node_a, node_b):
        node_a.add_connection(node_b)
        node_b.add_connection(node_a)

    def get_structure(self):
        network = {"nodes": [], "edges": []}
        for node in self.nodes:
            network["nodes"].append(node.name)
            for connection, weight in node.connections.items():
                print(weight)
                if weight > 0.8:
                    connection_tuple = (node.name, connection.name)
                    network["edges"].append(connection_tuple)
        return network

    def simulate_interactions(self, iterations):
        # Generate all possible non-repeating pairs
        pairs = list(itertools.combinations(self.nodes, 2))

        for _ in range(iterations):
            # Randomly shuffle these pairs
            random.shuffle(pairs)
            for pair in pairs:
                self.add_connection(pair[0], pair[1])


class Node:
    def __init__(self, bias, elasticity, name):
        self.bias = bias
        self.elasticity = elasticity
        self.connections = {}
        self.name = str(bias)[1:4]

    def has_connection(self, node):
        if node in self.connections:
            return self.connections[node]
        else:
            return False

    def add_connection(self, node):
        weight = self.get_connection_weight(node)
        self.connections[node] = weight
        #self.update_bias(node)

    def get_connection_weight(self, node):
        similarity = abs(node.bias - self.bias)
        weight = 1 - similarity
        if self.has_connection(node):
            return (weight + self.has_connection(node)) / 2
        else:
            return weight

    def update_bias(self, node):
        self.bias = (self.bias + node.bias) / 2


