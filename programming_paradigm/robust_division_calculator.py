def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator 
    except ZeroDivisionError:
        return f"Error: Cannot divide by zero"
    except ValueError:
        return f"please enter numeric values only"
    else: 
        return f"The result of the division is {result:.1f}"