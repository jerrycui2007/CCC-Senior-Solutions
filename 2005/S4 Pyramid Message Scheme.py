# https://dmoj.ca/problem/ccc05s4

l = int(input())


def reform_network(graph, start, visited):
    queue = []
    visited.add(start)
    queue.append(start)
    reformed_network = {}

    while len(queue) > 0:
        target = queue.pop(0)  # remove this target from the queue and then visit its neighbors
        if target not in reformed_network:
            reformed_network[target] = []

        for neighbor in graph[target]:
            if neighbor not in visited:
                visited.add(neighbor)  # mark the neighbors as visited and add it to the queue, if it hasn't been
                queue.append(neighbor)  # visited already
                reformed_network[target].append(neighbor)

    return reformed_network


def longest_path(network, start):
    distances = {}
    for worker in network:
        distances[worker] = 0
    queue = [start]
    longest_distance = 0

    while len(queue) > 0:
        target = queue.pop(0)
        for sub_ordinate in network[target]:
            distances[sub_ordinate] = distances[target] + 1
            if distances[sub_ordinate] > longest_distance:
                longest_distance = distances[sub_ordinate]
            queue.append(sub_ordinate)

    return longest_distance


def number_of_messages(network):
    total_messages = 0
    for worker in network:
        total_messages += len(network[worker])

    return total_messages


for _ in range(l):
    number_of_recipients = int(input())
    network = {}
    recipients = []
    reformed = {}

    for _ in range(number_of_recipients):
        recipients.append(input())
        network[recipients[-1]] = []
        reformed[recipients[-1]] = False

    for i in range(number_of_recipients - 1):
        if recipients[i + 1] not in network[recipients[i]]:
            network[recipients[i]].append(recipients[i + 1])
        if recipients[i] not in network[recipients[i + 1]]:
            network[recipients[i + 1]].append(recipients[i])

    leader = recipients[-1]  # always the last one is the leader
    reformed_network = reform_network(network, leader, set())

    new_time = longest_path(reformed_network, leader) * 20
    old_time = number_of_messages(network) * 10

    print(old_time - new_time)