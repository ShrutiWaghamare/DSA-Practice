m = int(input())
curr_pass = 0
max_pass = 0
for i in range(m):
    get_off, get_on = map(int, input().split())
    curr_pass = curr_pass - get_off + get_on
    if curr_pass>max_pass:
        max_pass = curr_pass
print(max_pass)
# buss passenger tracking