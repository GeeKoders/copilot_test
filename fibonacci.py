def fibonacci(n):
    """
    Calculates the nth Fibonacci number using a recursive approach.

    Args:
        n (int): The position in the Fibonacci sequence (must be a non-negative integer).

    Returns:
        int: The nth Fibonacci number. Returns 0 if n <= 0.

    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(5)
        5
    """
    # Recursive implementation with base case handling
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print(fibonacci(10))  # Example usage
    print(fibonacci(20))  # Example usage
    print(fibonacci(30))  # Example usage
    print(fibonacci(40))  # Example usage
    print(fibonacci(50))  # Example usage



