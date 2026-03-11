msg = input()
count = 1
for i in range(1, len(msg)):
    if msg[i] == msg[i-1]:
        count += 1
    else:
        count -= 1
        
    if count >= 3:
        print("Spam")
        break
else:
    print("Safe")