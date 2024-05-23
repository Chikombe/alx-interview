#!/usr/bin/python3
def validUTF8(data):
    """
    Validate if a given dataset represents a valid UTF-8 encoding.

    :param data: List[int] - a list of integers representing bytes
    :return: bool - True if the data is a valid UTF-8 encoding, else False
    """
    n_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        if byte > 255:
            return False

        mask = 1 << 7
        if n_bytes == 0:
            # Count the number of 1s from the most significant bit
            while mask & byte:
                n_bytes += 1
             mask = mask >> 1
            
            if n_bytes == 0:
                continue
            
            if n_bytes == 1 or n_bytes > 4:
                return False
            
        else:
            # For remaining bytes, they must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        
        n_bytes -= 1

    return n_bytes == 0
