#!/bin/python3

def is_possible(game, red_count, green_count, blue_count):
    cube_counts = {'red': red_count, 'green': green_count, 'blue': blue_count}

    for subset in game:
        subset_counts = {}
        for item in subset:
            count, color = item.split()
            subset_counts[color] = subset_counts.get(color, 0) + int(count)

        for color, count in subset_counts.items():
            if count > cube_counts[color]:
                return False

    return True

def possible_games(cube_counts, input_filename):
    possible_ids = []
    
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split(':')
        game_id = int(parts[0].split()[1])
        subsets = [subset.strip().split(', ') for subset in parts[1].strip().split(';')]
        
        if is_possible(subsets, *cube_counts):
            possible_ids.append(game_id)

    return possible_ids

red_count = 12
green_count = 13
blue_count = 14

input_filename = 'input'
if __name__ == '__main__':
    possible_ids = possible_games((red_count, green_count, blue_count), input_filename)

    sum_possible_ids = sum(possible_ids)

    print("Possible Games IDs:", possible_ids)
    print("Sum of Possible Game IDs:", sum_possible_ids)

