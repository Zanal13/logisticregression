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
