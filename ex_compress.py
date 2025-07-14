# compressing: aabbbcdddd becomes a2b3c1d4

def compress_string(s):
    result = ""
    i = 0

    while i < len(s):
        current_char = s[i]
        count = 1

        # Count how many times current_char repeats consecutively
        while i + count < len(s) and s[i + count] == current_char:
            count += 1

        result += current_char + str(count)
        i += count  # Skip over this group

    return result

def compress_back_string(s):
    #a2b3c4d1
    
    end = ""
    
    for i in range(0,len(s),2):
        letter = s[i]
        occ = s[i+1]
        repeat = letter * int(occ)
        end += repeat
        
    return end



# main program
val = input("Give a set of characters: ")
final = compress_string(val)
print(val, "becomes", final)

back = compress_back_string(final)
print("\ncompressed again: ", back)

