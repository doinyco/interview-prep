# Write a function to find the square root of a number.

def square_root(n):
    if n < 0:
        return "Invalid input"
    
    max_val = n
    min_val = 0
    result = (max_val + min_val) / 2  # Initialize properly
    estimate = result * result - n  # Initial estimate

    while abs(estimate) > 0.001:  # Ensure proper stopping condition
        result = (max_val + min_val) / 2  # Corrected typo here
        estimate = result * result - n  # Update estimate
        if estimate > 0:
            max_val = result
        else:
            min_val = result

    return result

# Test square_root function
print(square_root(16)) # 4.0