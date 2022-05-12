from operator import le
import re


ERROR_MESSAGE = "No se puede cubrir la ruta"


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

def there_are_antennas(available_antennas):
    return not len(available_antennas) == 0

def can_cover_road_length(available_antennas, k):
    return not max(available_antennas, key=lambda x: x[2])[2] < k


def start_can_be_covered(available_antennas):
    return not available_antennas[0][1] > 0


def check_border_cases(available_antennas, k):
    return there_are_antennas(available_antennas) and can_cover_road_length(available_antennas, k) and start_can_be_covered(available_antennas)



def best_contracts(k, file_name):
    available_antennas = process_antennas(file_name)

    valid = check_border_cases(available_antennas, k)
    if not valid:
        return ERROR_MESSAGE

    contracts = []
    end_optimal_antenna = available_antennas[0][2]
    optimal_antenna = available_antennas[0]
    start = 0

    for i, antenna in enumerate(available_antennas[1:]):
        if route_is_covered(start, k):
            return  [contract[0] for contract in contracts]
        start_antenna = antenna[1]
        end_antenna = antenna[2]
        if start_antenna <= start and end_optimal_antenna <= end_antenna:
            end_optimal_antenna = end_antenna
            optimal_antenna = antenna
        elif start_antenna > start:
            start = end_optimal_antenna
            contracts.append(optimal_antenna)
            if route_is_covered(start, k):
                return  [contract[0] for contract in contracts]
            if start_antenna <= start:
                end_optimal_antenna = end_antenna
                optimal_antenna = antenna
            else:
                return ERROR_MESSAGE
    
    last_antennna = available_antennas[-1]
    if last_antennna[1] <= start:
        contracts.append(last_antennna)
    else:
        return ERROR_MESSAGE

    return  [contract[0] for contract in contracts]