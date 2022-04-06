def process_antennas(file_name):
    available_antennas = []

    with open(file_name) as file:
        contracts = file.readlines()

    for line in contracts:
        antenna = line.split(",")
        available_antennas.append((antenna[0], int(antenna[1]) - int(antenna[2]), int(antenna[1]) + int(antenna[2])))

    available_antennas.sort(key=lambda x: x[1])

    return available_antennas


def route_is_covered(start, k):
    return start >= k


def best_contracts(k, file_name):
    available_antennas = process_antennas(file_name)

    if max(available_antennas, key=lambda x: x[2])[2] < k:
        return "No se puede cubrir la ruta completamente"

    contracts = []
    optimal_antenna = available_antennas[0]
    start = 0

    for i, antenna in enumerate(available_antennas[1:]):
        if route_is_covered(start, k):
            continue
        if antenna[1] <= start and optimal_antenna[2] <= antenna[2]:
            optimal_antenna = antenna
        elif antenna[1] > start:
            start = optimal_antenna[2]
            contracts.append(optimal_antenna)

            optimal_antenna = antenna
            if i == len(available_antennas) - 2 and contracts[-1][2] < k:
                contracts.append(antenna)

    return [contract[0] for contract in contracts]