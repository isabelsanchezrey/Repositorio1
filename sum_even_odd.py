# sum_even_odd.py
# Este script calcula la suma de los números pares e impares en una lista dada.

def sum_even_odd(numbers):
    """
    Calcula la suma de números pares e impares en una lista.
    
    Args:
        numbers (list): Lista de números enteros.

    Returns:
        dict: Un diccionario con las sumas de números pares e impares.
    """
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    
    return {"even_sum": even_sum, "odd_sum": odd_sum}


if __name__ == "__main__":
    # Lista de ejemplo
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sum_even_odd(numbers)

    print("Lista de números:", numbers)
    print("Suma de números pares:", result["even_sum"])
    print("Suma de números impares:", result["odd_sum"])
