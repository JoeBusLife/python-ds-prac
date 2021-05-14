def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap_low = to_swap.lower()
    output = ""
    
    for let in phrase:
        if let.lower() == to_swap_low:
            output += let.swapcase()
        else:
            output += let
        
    return output