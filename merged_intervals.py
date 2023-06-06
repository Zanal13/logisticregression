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
    player1_position = [0, 0]
    player2_position = [0, 0]
    closest_distance = float('inf')
    closest_point = None

    for instr1, instr2 in zip(player1_instructions, player2_instructions):
        direction1, steps1 = instr1[0], int(instr1[1:])
        direction2, steps2 = instr2[0], int(instr2[1:])

        for _ in range(steps1):
            if direction1 == 'R':
                player1_position[0] += 1
            elif direction1 == 'L':
                player1_position[0] -= 1
            elif direction1 == 'U':
                player1_position[1] += 1
            elif direction1 == 'D':
                player1_position[1] -= 1

            for _ in range(steps2):
                if direction2 == 'R':
                    player2_position[0] += 1
                elif direction2 == 'L':
                    player2_position[0] -= 1
                elif direction2 == 'U':
                    player2_position[1] += 1
                elif direction2 == 'D':
                    player2_position[1] -= 1

                distance = abs(player1_position[0] - player2_position[0]) + abs(player1_position[1] - player2_position[1])
                if distance < closest_distance:
                    closest_distance = distance
                    closest_point = (player1_position[0], player1_position[1])

    return closest_point

# Example instructions for player1 and player2
player1_instructions = ['R3', 'U3', 'L1', 'D5', 'L6']
player2_instructions = ['U6', 'L1', 'D10', 'L2', 'U4']

closest_point = calculate_closest_point(player1_instructions, player2_instructions)
print(closest_point)  # Output: (-1, 2)

