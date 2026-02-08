def canJump(nums):
    """
    You are standing at index 0.
    Each nums[i] tells the maximum jump length from index i.
    The goal is to reach the last index.
    """

    # maxReach stores the farthest index we can reach so far
    maxReach = 0

    # Traverse the array index by index
    for i in range(len(nums)):

        # If current index is greater than what we can reach,
        # it means we are stuck and cannot move further
        if i > maxReach:
            return False

        # From index i, the farthest we can jump is:
        # current index + jump length at this index
        # We update maxReach with the maximum reachable index
        maxReach = max(maxReach, i + nums[i])

    # If we finish the loop, it means we never got stuck
    # Hence, we can reach the last index
    return True


# Example test cases
print(canJump([2, 3, 1, 1, 4]))  # True
print(canJump([3, 2, 1, 0, 4]))  # False
