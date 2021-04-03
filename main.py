import random


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


def calculate_cost(route):
    cost = 0
    for i in range(0, n):
        city_A = route[i - 1]
        city_B = route[i]
        cost = cost + cities[city_A][city_B]
    return cost


def generate_random_route(number_of_cities):
    l = list(range(number_of_cities))
    random.shuffle(l)
    return l


def generate_random_cities(number_of_cities):
    cities = [[0 for i in range(number_of_cities)] for j in range(number_of_cities)]
    for i in range(0, number_of_cities):
        for j in range(0, number_of_cities):
            if i > j:
                random_number = random.randint(1, 50)
                cities[i][j] = random_number
                cities[j][i] = random_number
    return cities


def generate_neighbors(route, n):
    my_neighbors = []
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            new_neighbor = swapPositions(route, i, j).copy()
            my_neighbors.append(new_neighbor)

    return my_neighbors


n = int(input("Please Insert the number of cities: "))

cities = generate_random_cities(n)
# for i in range(0, n):
#     print(cities[i])

random_route = generate_random_route(n)
# print(random_route)

cost = calculate_cost(random_route)
# print(cost)

# neighbors = generate_neighbors(random_route, n)
# print(neighbors)

best_route = random_route

while True:
    cost = calculate_cost(best_route)
    neighbors = generate_neighbors(best_route, n)
    best_cost = cost
    for route in neighbors:
        new_route_cost = calculate_cost(route)
        if new_route_cost < best_cost:
            best_route = route.copy()
            best_cost = new_route_cost
    if best_cost == cost:
        break
print("Best Route is: ", end='')
print(best_route)
print("Best Cost is: ", end='')
print(best_cost)
