from operator import le
import re
from exceptions import *


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
    if len(available_antennas) == 0:
        raise NoAntennaException(ERROR_MESSAGE)

def can_cover_road_length(available_antennas, k):
    if max(available_antennas, key=lambda x: x[2])[2] < k:
        raise LongRoadException(ERROR_MESSAGE)


def start_can_be_covered(available_antennas):
    if available_antennas[0][1] > 0:
        raise StartIsNotCovered(ERROR_MESSAGE)


def check_border_cases(available_antennas, k):
    there_are_antennas(available_antennas) 
    can_cover_road_length(available_antennas, k) 
    start_can_be_covered(available_antennas)



def best_contracts(k, file_name):
    available_antennas = process_antennas(file_name)

    check_border_cases(available_antennas, k)

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
                raise Exception(ERROR_MESSAGE)
    
    last_antennna = available_antennas[-1]
    if last_antennna[1] <= start:
        contracts.append(last_antennna)
    else:
        return Exception(ERROR_MESSAGE)

    return  [contract[0] for contract in contracts]