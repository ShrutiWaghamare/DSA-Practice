def suminrotate(nums, target):
    n = len(nums)

    # 1️⃣ Find pivot (largest element)
    # pivot = -1
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            pivot = i
            break

    # If array is not rotated
    # if pivot == -1:
    #     pivot = n - 1

    # 2️⃣ Initialize pointers
    left = (pivot + 1) % n   # smallest element
    right = pivot            # largest element

    # 3️⃣ Two-pointer search
    while left != right:
        cur_sum = nums[left] + nums[right]

        if cur_sum == target:
            return True
        elif cur_sum < target:
            left = (left + 1) % n
        else:
            right = (right - 1 + n) % n

    return False


# 🔹 Test
nums = [11, 15, 6, 8, 9, 10]
target = 16

print(suminrotate(nums, target))  # True
