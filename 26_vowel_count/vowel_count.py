def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    VOWELS = set("aeiou")
    phrase_low = phrase.lower()
    result = {}
    
    for let in phrase_low:
        if let in VOWELS:
            result[let] = result.get(let, 0) + 1
            # result[let] = result[let] + 1 if result[let] else 1
    
    return result
    
    # {let: +=1 for let in phrase_low if let in VOWELS}