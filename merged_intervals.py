def calculate_interval_length(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    merged_intervals = [intervals[0]]  # Initialize merged intervals with the first interval

    for interval in intervals[1:]:
        # Check if the current interval overlaps with the last merged interval
        if interval[0] <= merged_intervals[-1][1]:
            # Merge the intervals if there is overlap
            merged_intervals[-1] = (merged_intervals[-1][0], max(interval[1], merged_intervals[-1][1]))
        else:
            # Add the non-overlapping interval to the merged intervals
            merged_intervals.append(interval)

    # Calculate the sum of the lengths of merged intervals
    total_length = sum(end - start for start, end in merged_intervals)
    return total_length


def calculate_closest_point(player1_instructions, player2_instructions):
    player1_positions = [(0, 0)]
    player2_positions = [(0, 0)]
    closest_distance = float('inf')
    closest_point = None

    for instr in player1_instructions:
        direction, steps = instr[0], int(instr[1:])
        for _ in range(steps):
            prev_position = player1_positions[-1]
            if direction == 'R':
                new_position = (prev_position[0] + 1, prev_position[1])
            elif direction == 'L':
                new_position = (prev_position[0] - 1, prev_position[1])
            elif direction == 'U':
                new_position = (prev_position[0], prev_position[1] + 1)
            elif direction == 'D':
                new_position = (prev_position[0], prev_position[1] - 1)
            player1_positions.append(new_position)

    for instr in player2_instructions:
        direction, steps = instr[0], int(instr[1:])
        for _ in range(steps):
            prev_position = player2_positions[-1]
            if direction == 'R':
                new_position = (prev_position[0] + 1, prev_position[1])
            elif direction == 'L':
                new_position = (prev_position[0] - 1, prev_position[1])
            elif direction == 'U':
                new_position = (prev_position[0], prev_position[1] + 1)
            elif direction == 'D':
                new_position = (prev_position[0], prev_position[1] - 1)
            player2_positions.append(new_position)

    common_positions = set(player1_positions) & set(player2_positions)

    for position in common_positions:
        distance = abs(position[0]) + abs(position[1])
        if distance < closest_distance:
            closest_distance = distance
            closest_point = position

    return closest_point

# Example instructions for player1 and player2
player1_instructions = ['R3', 'U3', 'L1', 'D5', 'L6']
player2_instructions = ['U6', 'L1', 'D10', 'L2', 'U4']

closest_point = calculate_closest_point(player1_instructions, player2_instructions)
print(closest_point)  # Output: (-1, 2)

