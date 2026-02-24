def freqChar(s):
    result = ""
    freq = {}
    for ch in s:
        if ch == " ":
            continue
        freq[ch] = freq.get(ch, 0) + 1
    
    # sorted_freq = sorted(freq.items(), key = lambda x : x[1])
    # for ch, count in sorted_freq:
    #     result += ch * count
    
    # return result
    return "".join(ch * count for ch, count in sorted(freq.items(), key = lambda x : x[1]) )
        
s = "geeks for geeks"
print(freqChar(s))