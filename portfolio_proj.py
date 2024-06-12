# Importing necessary libraries
import numpy as np

def calculate_area(radius):
    """
    Function to calculate the area of a circle given its radius.
    
    Args:
    radius (float): The radius of the circle
    
    Returns:
    float: The area of the circle
    """
    # Area of a circle formula: πr^2
    area = np.pi * radius ** 2
    return area

def main():
    """
    Main function to demonstrate the use of calculate_area.
    """
    # Example radius
    radius = 5.0
    
    # Calculate the area using the calculate_area function
    area = calculate_area(radius)
    
    # Print the result
    print(f"The area of the circle with radius {radius} is {area:.2f} square units.")

# Entry point of the script
if __name__ == "__main__":
    main()
