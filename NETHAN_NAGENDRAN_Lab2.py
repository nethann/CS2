def get_v2c_ratio(string):
    vowels_counter = 0
    consonants_counter = 0
    vowels = 'aeiou'
    for characters in string:
        if characters.isalpha(): 
            if characters.lower() in vowels:
                vowels_counter += 1
            else:
                consonants_counter += 1
    
    final_ratio = vowels_counter / consonants_counter
    
    print(f"{final_ratio:.2f}")


def get_longest_run_length(string):
    longest_sequence = ""
    sequence = ""
    previous_char = ""

    longest_char_iterate_counter = 0

    for characters in string:
        if characters == previous_char:
            sequence += characters
        else:
            if len(sequence) > len(longest_sequence):
                longest_sequence = sequence
            sequence = characters

        previous_char = characters

    if len(sequence) > len(longest_sequence):
        longest_sequence = sequence

    for elements in longest_sequence: 
        longest_char_iterate_counter += 1

    return longest_char_iterate_counter


#outputs for function 1
get_v2c_ratio("abcacdae")
get_v2c_ratio("abcabcabcxyz")

#output sfor function 2
print(get_longest_run_length("ddddddddeeffc"))
print(get_longest_run_length("abcde"))
