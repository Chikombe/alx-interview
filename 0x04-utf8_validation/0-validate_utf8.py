#!/usr/bin/python3
"""UTF-8 validation module.
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    n = len(data)
    for i in range(n):
        if skip > 0:
            skip -= 1
            continue

        byte = data[i]
        if type(byte) != int or byte < 0 or byte > 255:
            return False

        # Determine the number of bytes in the character
        if byte <= 0x7F:
            # 1-byte character
            skip = 0
        elif byte & 0b11111000 == 0b11110000:
            # 4-byte character
            span = 4
            if n - i >= span:
                next_bytes = data[i + 1:i + span]
                if not all((next_byte & 0b11000000) == 0b10000000 for next_byte in next_bytes):
                    return False
                skip = span - 1
            else:
                return False
        elif byte & 0b11110000 == 0b11100000:
            # 3-byte character
            span = 3
            if n - i >= span:
                next_bytes = data[i + 1:i + span]
                if not all((next_byte & 0b11000000) == 0b10000000 for next_byte in next_bytes):
                    return False
                skip = span - 1
            else:
                return False
        elif byte & 0b11100000 == 0b11000000:
            # 2-byte character
            span = 2
            if n - i >= span:
                next_bytes = data[i + 1:i + span]
                if not all((next_byte & 0b11000000) == 0b10000000 for next_byte in next_bytes):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
