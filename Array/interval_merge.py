def intervalmerge(intervals):
    intervals.sort(key = lambda x : x[0])
    current = intervals[0]
    result = []
    for next_int in intervals[1:]:
        if next_int[0] <= current[1]:
            current[1] = max(current[1], next_int[1])
        else:
            result.append(current)
            current = next_int
        result.append(current)
    return result
    
intervals = [[1, 3], [2, 6] [8,10], [15, 18]]
print(intervalmerge(intervals))