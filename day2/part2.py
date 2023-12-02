#!/bin/python3

def is_possible(game):
    cube_counts = {'red': 0, 'green': 0, 'blue': 0}
    result = 1

    for subset in game:
        subset_counts = {}
        for item in subset:
            count, color = item.split()
            subset_counts[color] = subset_counts.get(color, 0) + int(count)
        for color, count in subset_counts.items():
            if count > cube_counts[color]:
                cube_counts[color] = count
    for i in list(cube_counts.values()):
        result *= i
    return result


def possible_games(input_filename):
    possible= [] 
    
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split(':')
        game_id = int(parts[0].split()[1])
        subsets = [subset.strip().split(', ') for subset in parts[1].strip().split(';')]
        possible.append(is_possible(subsets))
    return possible



input_filename = './input'
if __name__ == '__main__':
    possible= possible_games(input_filename)
    print(sum(possible))




