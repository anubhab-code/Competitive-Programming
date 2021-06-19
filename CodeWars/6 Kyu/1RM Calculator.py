def calculate_1RM(a, b):
    return (
        a if b == 1 else
        0 if b == 0 else
        round(max(
            a * (1 + b/30),
            100 * a / (101.3 - 2.67123*b),
            a * b**0.10,
        ))
    )