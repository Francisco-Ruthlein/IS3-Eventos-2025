def suma(a, b):
    try:
        if a is None or b is None:
            return None
        return int(a) + int(b)
    except (ValueError, TypeError):
        return None

# Nuevas funciones para probar
def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def cuadrado_binomio(a, b):
    # (a + b)^2 = a² + 2ab + b²
    a_cuadrado = multiplicacion(a, a)
    dos_ab = multiplicacion(2, multiplicacion(a, b))
    b_cuadrado = multiplicacion(b, b)
    return (a_cuadrado, dos_ab, b_cuadrado)  # Retorna una tupla con los componentes
