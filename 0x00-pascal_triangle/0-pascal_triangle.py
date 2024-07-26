#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's Triangle with n rows.

    Args:
    n (int): The number of rows in Pascal's Triangle.

    Returns:
    list: A list of lists representing Pascal's Triangle.
    """
    # Return an empty list if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle as an empty list
    triangle = []

    # Iterate over each row from 0 to n-1
    for row_number in range(n):
        # Start each row with 1s
        row = [1] * (row_number + 1)

        # Calculate the interior values of the row
        for j in range(1, row_number):
            # Each interior value is the sum of the two values above it
            row[j] = (triangle[row_number - 1][j - 1] +
                      triangle[row_number - 1][j])

        # Append the completed row to the triangle
        triangle.append(row)

    return triangle
