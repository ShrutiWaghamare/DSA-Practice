start = int(input("Enter start: ")) 
end = int(input("Enter end: "))
for num in range(start, end + 1):
    if num % 7 != 0:
        continue
    if num % 5 == 0:
        continue
    s = str(num)
    if s == s[::-1]:
        continue
    if len(s) != len(set(s)):
        continue
    print(num, end= " ")
    