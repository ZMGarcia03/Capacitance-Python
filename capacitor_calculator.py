def calculate_capacitance(resistance, time_constant):
    """
    Calculate the needed capacitance value.

    Parameters:
    resistance (float): The resistance in ohms.
    time_constant (float): The time constant in seconds.

    Returns:
    float: The capacitance value in farads.
    """
    if resistance <= 0:
        raise ValueError("Resistance must be greater than zero.")
    if time_constant <= 0:
        raise ValueError("Time constant must be greater than zero.")

    capacitance = time_constant / resistance
    return capacitance

def main():
    try:
        # Get input values from the user
        resistance = float(input("Enter the resistance (R) in ohms: "))
        time_constant = float(input("Enter the time constant (τ) in seconds: "))

        # Calculate capacitance
        capacitance = calculate_capacitance(resistance, time_constant)

        # Output the result
        print(f"The needed capacitance value is: {capacitance:.6f} farads")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
