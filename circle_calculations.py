# circle_calculations.py
# Este script calcula el área y el perímetro de un círculo dado su radio.

import math

def calculate_circle(radius):
    """
    Calcula el área y el perímetro de un círculo dado su radio.

    Args:
        radius (float): El radio del círculo.

    Returns:
        dict: Un diccionario con el área y el perímetro del círculo.
    """
    if radius < 0:
        return {"error": "El radio no puede ser negativo."}
    
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return {"area": area, "perimeter": perimeter}


if __name__ == "__main__":
    # Pedir al usuario que ingrese el radio
    try:
        radius = float(input("Introduce el radio del círculo: "))
        result = calculate_circle(radius)

        if "error" in result:
            print(result["error"])
        else:
            print(f"Para un círculo con radio {radius}:")
            print(f"- Área: {result['area']:.2f}")
            print(f"- Perímetro: {result['perimeter']:.2f}")
    except ValueError:
        print("Por favor, introduce un número válido.")
