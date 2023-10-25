def fahrenheit_to_celsius(fahrenheit):
    """Converts a temperature from Fahrenheit to Celsius.

    Args:
      fahrenheit: A single floating-point number representing a temperature in
        Fahrenheit.

    Returns:
      The temperature converted to Celsius.
    """

    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
