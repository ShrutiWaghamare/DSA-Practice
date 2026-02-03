# -----------------------------
# BRUTE FORCE APPROACH
# -----------------------------
def merge_bruteforce(intervals):
    intervals = sorted(intervals, key=lambda x: x[0])
    
    changed = True
    while changed:
        changed = False
        result = []
        i = 0
        
        while i < len(intervals):
            cur = intervals[i]
            j = i + 1
            
            while j < len(intervals) and intervals[j][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[j][1])
                j += 1
                changed = True
            
            result.append(cur)
            i = j
        
        intervals = result
    
    return intervals


# -----------------------------
# OPTIMAL APPROACH
# -----------------------------
def merge_optimal(intervals):
    intervals.sort(key=lambda x: x[0])
    
    result = []
    curr_int = intervals[0]
    
    for next_int in intervals[1:]:
        if next_int[0] <= curr_int[1]:
            curr_int[1] = max(curr_int[1], next_int[1])
        else:
            result.append(curr_int)
            curr_int = next_int
    
    result.append(curr_int)
    return result


# -----------------------------
# TEST
# -----------------------------
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

print("Brute Force Result :", merge_bruteforce(intervals.copy()))
print("Optimal Result     :", merge_optimal(intervals.copy()))
